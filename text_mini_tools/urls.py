from django.urls import path
from . import views

urlpatterns = [
    path('', views.char_counter, name='Char counter'),
]
