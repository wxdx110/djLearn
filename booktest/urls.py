from django.contrib import admin
from django.urls import *
from booktest import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(\d+)$', views.show)
]