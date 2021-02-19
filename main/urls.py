# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'), # id from url is passed to views.index
]