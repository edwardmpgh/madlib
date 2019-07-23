from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, HTML, ButtonHolder, Field, Fieldset, Hidden
from crispy_forms.bootstrap import FormActions, FieldWithButtons, StrictButton, InlineCheckboxes

from .models import MadLibs, WordType

# add a new event
class MadLibForm(forms.ModelForm):
    class Meta:
        model = MadLibs
        fields = ['madlib',]

    def __init__(self, *args, **kwargs):
        super(MadLibForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.fields['madlib'].placeholder = 'Enter you MabLib'
        self.helper.layout = Layout(
            'madlib',
        )


# add a new event
class WordTypeForm(forms.ModelForm):
    class Meta:
        model = WordType
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(WordTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'description',
        )