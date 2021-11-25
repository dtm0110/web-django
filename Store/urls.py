from django import urls
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views
from .views import home

urlpatterns = [
    path('search/', views.search, name='search'),
    path('',home,name="home"),
] 