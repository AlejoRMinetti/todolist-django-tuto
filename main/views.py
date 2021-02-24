# views.py file
from django.shortcuts import render
from .models import ToDoList, Item


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls}) # dictionary to use in the html 


def home(response):
    return render(response, "main/home.html", {})