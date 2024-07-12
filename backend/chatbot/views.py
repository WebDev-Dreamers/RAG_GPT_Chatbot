from django.shortcuts import render
from .rag_model import *
from .views import *
from .forms import *

import os
from django.conf import settings
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

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



#################### 2. 대화형 chatbot #################### 
def interactive_chatbot(request):
    
    global memory

    # URL 페이지 방문
    if request.method == 'GET':

        # Memory 초기화 (처음에만 대화 초기화)
        memory = new_memory()
        
        # 입력 Form
        form = HisotryModelForm()
        
        # 대화 흐름 세션에서 가져오기
        chat_history = request.session.get('chat_history',[])
        
        context = {
            'form':form,
            'chat_history': chat_history,
        }

        return render(request, 'chatbot/interactive_chatbot.html', context)
    
    else:
        
        # chatbot 생성 (대화 흐름 기억)
        chatbot = rag_gpt_chatbot(memory)
        
        # 질의 가져오기
        query = request.POST.get('question')
        answer = chatbot(query)                         # Chatbot 답변 생성
        
        # 대화 흐름 세션에서 가져와서 (질의 - 응답) 추가
        chat_history = request.session.get('chat_history',[])
        chat_history.append({'question': query, 'answer': answer['answer']})
        request.session['chat_history'] = chat_history
        
        context = {
            'chat_history': chat_history
        }
    
        # History 모델에 저장하기
        history = History()
        history.question = query
        history.answer = answer['answer']
        history.save()
        
        return render(request, 'chatbot/interactive_chatbot.html', context)




#################### 3. 커스텀 chatbot #################### 
def custom_chatbot(request):
    
    global memory

    # URL 페이지 방문
    if request.method == 'GET':

        # Memory 초기화 (처음에만 대화 초기화)
        memory = new_memory()
        
        # 입력 Form
        form = HisotryModelForm()
        
        # 대화 흐름 세션에서 가져오기
        chat_history = request.session.get('chat_history',[])
        
        context = {
            'form':form,
            'chat_history': chat_history,
        }

        return render(request, 'chatbot/custom_chatbot.html', context)
    
    else:
        
        # chatbot 생성 (대화 흐름 기억)
        chatbot = rag_gpt_chatbot(memory)
        
        # 질의 가져오기
        query = request.POST.get('question')
        answer = chatbot(query)                         # Chatbot 답변 생성
        
        # 대화 흐름 세션에서 가져와서 (질의 - 응답) 추가
        chat_history = request.session.get('chat_history',[])
        chat_history.append({'question': query, 'answer': answer['answer']})
        request.session['chat_history'] = chat_history
        
        context = {
            'chat_history': chat_history
        }
    
        # History 모델에 저장하기
        history = History()
        history.question = query
        history.answer = answer['answer']
        history.save()
        
        return render(request, 'chatbot/custom_chatbot.html', context)

def add_vectorDB(request):

    if request.method == 'POST':

        # 파일 입력
        file = request.FILES['file']

        # QA csv 파일
        if file.name.endswith('.csv'):

            file_path = os.path.join(settings.BASE_DIR, 'csvFiles', file.name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            # CSV 파일 읽기
            data = pd.read_csv(file_path)

            # 첫 번째 열을 '구분', 두 번째 열을 'QA'로 간주
            category_list = data.iloc[:, 0].tolist()
            text_list = data.iloc[:, 1].tolist()

            # Document 객체 생성
            documents = [Document(page_content=text, metadata={'category': category}) for text, category in zip(text_list, category_list)]
            
            # 데이터베이스 초기화
            embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
            database = Chroma(persist_directory="./vectorDB", embedding_function=embeddings)
            
            new_documents = []
            for doc in documents:
                qa_text = doc.page_content
                # 유사도 측정
                results = database.similarity_search_with_score(qa_text, k=3)
                scores = [score for _, score in results]
                
                # 유사하지 않다면 새 항목으로 추가
                if all(score > 0.35 for score in scores):
                    new_documents.append(doc)
            
            # 새로운 데이터 추가
            if new_documents:
                database.add_documents(new_documents)
            
            return render(request, 'chatbot/custom_chatbot.html', {'message': '새로운 데이터가 Vector DB에 추가되었습니다!'})
        
    return render(request, 'chatbot/add_vectorDB.html')