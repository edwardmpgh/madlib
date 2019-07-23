from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.utils import timezone

from .forms import MadLibForm, WordTypeForm
from .models import MadLibs, IpAddress, WordType, GameParameters


def get_parameter_value(parameter_name):
    p = GameParameters.objects.get(parameter=parameter_name)
    if p:
        return p.parameter_value
    else:
        return None


def set_parameter_value(parameter_name, parameter_value):
    p = GameParameters.objects.get(parameter=parameter_name)
    if p:
        p.parameter_value = parameter_value
        p.save()


def index(request):
    current_user = request.user

    context = dict()

    if request.method == 'POST':
        ml = MadLibs()
        form = MadLibForm(request.POST or None, instance=ml)
        if form.is_valid():
            form.save()

    form = MadLibForm()

    context['form'] = form

    if current_user:
        context['word_types'] = WordType.objects.all()

    return render(request, 'public/index.html', context)


# def get_madlib_list(request):
#     return JsonResponse(madlib_list, safe=False)

def get_madlib_list(request):

    madlibs = MadLibs.objects.all()
    obj = []
    if not madlibs:
        obj.append('NO MADLIBS')
    for madlib in madlibs:
        button = ''
        if madlib.votes > 0:
            url = reverse('vote', args=[madlib.id])
            button += '<a class="btn btn-success btn-lg" href="%s">%s (%s)</a>' % (url, madlib.madlib, madlib.votes)
        else:
            url = reverse('vote', args=[madlib.id])
            button += '<a class="btn btn-outline-secondary btn-lg primary-color" href="%s">%s</a>' % (url, madlib.madlib)
        obj.append(button)
    return JsonResponse(obj, safe=False)


def get_madlib_list_gamemaster(request):

    madlibs = MadLibs.objects.all()
    obj = []
    if not madlibs:
        obj.append('NO MADLIBS')
    for madlib in madlibs:
        button = ''
        if madlib.votes > 0:
            url = reverse('declare_winner', args=[madlib.id])
            button += '<a class="btn btn-success btn-lg" href="%s">%s (%s)</a>' % (url, madlib.madlib, madlib.votes)
        obj.append(button)
    return JsonResponse(obj, safe=False)


def get_current_word_type(request):
    obj = []
    try:
        c_wt = get_parameter_value('c_word_type')
        wt = WordType.objects.get(id=int(c_wt))
        obj.append('<h2>%s</h2> <p>%s</p>' % (wt.name, wt.description))
        return JsonResponse(obj, safe=False)
    except:
        pass

    obj.append('<h2>No Current Word</h2>')
    return JsonResponse(obj, safe=False)


def get_winner(request):
    obj = []
    try:
        winner = get_parameter_value('winner')
        if not winner == 'None':
            obj.append('<h2>%s</h2>' % winner)
            return JsonResponse(obj, safe=False)
    except:
        pass

    obj.append('<h2>No Current Winner</h2>')
    return JsonResponse(obj, safe=False)


def declare_winner(request, madlib_id):

    ml = MadLibs.objects.get(id=madlib_id)
    c_wt = get_parameter_value('c_word_type')
    wt = WordType.objects.get(id=int(c_wt))

    set_parameter_value('winner', '%s: %s' % (wt.name, ml.madlib))

    return HttpResponseRedirect(reverse('index'))


def vote(request, ml_id):

    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        i = IpAddress(ip=ip)
        i.save()
        ml = MadLibs.objects.get(id=ml_id)
        ml.up_vote()
    except:
        pass

    return HttpResponseRedirect(reverse('index'))


def new_word(request, word_type_id):
    # clear previous word
    MadLibs.objects.all().delete()
    IpAddress.objects.all().delete()
    word_type = WordType.objects.get(id=word_type_id)
    set_parameter_value('c_word_type', word_type.id)
    set_parameter_value('winner', 'None')

    return HttpResponseRedirect(reverse('index'))


def new_word_type(request):

    context = dict()

    form = WordTypeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))

    context['form'] = form
    context['form_title'] = 'New Word Type'
    context['button_title'] = 'Add'

    return render(request, 'public/generic_form.html', context)