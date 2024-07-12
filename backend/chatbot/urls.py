from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path("simple/", views.simple_chatbot, name='simple'),                  # 단순형 Chatbot
    path("interactive/", views.interactive_chatbot, name='interactive'),   # 대화형 Chatbot
    path("custom/", views.custom_chatbot, name='custom'),                  # 커스텀 Chatbot
    path('add_vectorDB/', views.add_vectorDB, name='add_vectorDB')
]

