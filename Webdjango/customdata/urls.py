from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'appdata'

urlpatterns = [
    path('', views.index),
    path('csvget', views.getCsv, name = 'csvget'),

]