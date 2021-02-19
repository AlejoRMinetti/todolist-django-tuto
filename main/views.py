# views.py file
from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDoList, Item


def index(request, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><h3>%s</h3>" %(ls.name, item.text))