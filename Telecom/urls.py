from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.telecom_homepage, name='telecom_homepage'),
    url(r'result/', views.telecom_result, name='telecom_result'),
    url(r'model_analysis/', views.model_analysis, name='model_analysis'),
]