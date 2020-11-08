from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def telecom_homepage(request):
    return render(request, "Telecom/index.html")