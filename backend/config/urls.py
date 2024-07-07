from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path("", index, name='index'),                      # Default (메인 페이지)
    path("admin/", admin.site.urls),
    path("connection/", include('connection.urls')),    # Client 서버 통신
    path("chatbot/", include('chatbot.urls')),          # RAG_GPT Chatbot
]
