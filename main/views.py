# views.py file
from django.http import HttpResponse


def index(request, id):
    return HttpResponse("<h1>%s</h1>" % id)