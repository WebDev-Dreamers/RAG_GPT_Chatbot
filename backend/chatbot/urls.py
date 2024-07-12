from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path("simple/", views.simple_chatbot, name='simple'),         # 단순형 Chatbot
]
