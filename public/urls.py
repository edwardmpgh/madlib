from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_madlibs/', views.get_madlib_list, name='get_madlib_list'),
    path('vote/<int:ml_id>/', views.vote, name='vote'),
    path('new/type/<int:word_type_id>/', views.new_word, name='new_word'),
    path('current/word/', views.get_current_word_type, name='get_current_word_type'),
    path('word/new/', views.new_word_type, name='new_word_type'),
    path('current/winner/', views.get_winner, name='get_winner'),
    path('declare/winner/<int:madlib_id>/', views.declare_winner, name='declare_winner'),
    path('get/madlib/gamemaster/', views.get_madlib_list_gamemaster, name='get_madlib_list_gamemaster'),

]
