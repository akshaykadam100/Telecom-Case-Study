from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.telecom_homepage, name='telecom_homepage'),
]