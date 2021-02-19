# views.py file
from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDoList, Item


def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.name)