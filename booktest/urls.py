from django.contrib import admin
from django.urls import *
from booktest import views

urlpatterns = [
    # re_path(r'^(\d+)$', views.show)
    path('<int:id>/', views.show, name='show'), #int类型的id
]