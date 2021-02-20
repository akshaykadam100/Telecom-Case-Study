from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def analyzer_homepage(request):
    return HttpResponse("<h1>Hello</h1>")