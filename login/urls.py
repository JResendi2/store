from django.contrib import admin
from django.urls import path
from . import views;

urlpatterns = [
    path('', views.login_in, name="login_in"),
    path('login_up/', views.login_up, name="login_up"),
    path('loggedin_user/', views.loggedin_user, name="loggedin_user"),
    path('login_up_client/', views.login_up_client, name="login_up_client"),
    path('login_in_client/', views.login_in_client, name="login_in_client"),
]
