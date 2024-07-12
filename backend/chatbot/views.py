from django.shortcuts import render
from .rag_gpt_model import *
from .views import *
from .forms import *


# 대화 흐름 Memory
memory = None

#################### 1. 단순형 chatbot #################### 
def simple_chatbot(request):
    
    global memory

    # Memory 초기화 (새로운 대화)
    memory = new_memory()
    
    # URL 페이지 방문
    if request.method == 'GET':
        
        # 입력 Form
        form = HisotryModelForm()

        context = {
            'form':form,
        }

        return render(request, 'chatbot/simple_chatbot.html', context)
    
    else:
        
        # chatbot 생성 (대화 흐름 기억)
        chatbot = rag_gpt_chatbot(memory)

        # 질의 가져오기
        query = request.POST.get('question')
        answer = chatbot(query)                 # Chatbot 답변 생성        
        
        context = {
            'question': query,
            'answer' : answer['answer']
        }
    
        # History 모델에 저장하기
        history = History()
        history.question = query
        history.answer = answer['answer']
        history.save()
        
        return render(request, 'chatbot/simple_chatbot.html', context)



