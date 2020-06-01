from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('post', views.post, name='post'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]