# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>', views.index, name='index'), # name list from url is passed to views.index
]