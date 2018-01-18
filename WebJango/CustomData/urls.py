from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'appdata'

urlpatterns = [
    url('', views.index),
    url('search', views.search, name = 'search'),
]
