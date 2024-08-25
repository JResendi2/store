from django.urls import path
from .views import APIChatbot;
from . import views;


urlpatterns = [
    path('', APIChatbot.as_view(), name="chat"),
    path('create', views.createCredentials, name="create"),
]
   