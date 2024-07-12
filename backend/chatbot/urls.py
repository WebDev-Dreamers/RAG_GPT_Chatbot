from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path("simple/", views.simple_chatbot, name='simple'),         # 단순형 Chatbot
    path("interactive/", views.interactive_chatbot, name='interactive'),         # 단순형 Chatbot
]

