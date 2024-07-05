from django.shortcuts import render, HttpResponse

# Create your views here.
def connection(request):
    
    if request.method == "GET":
        
        print('연결 완료')
        
        return HttpResponse('연결 완료')

    else:
        return HttpResponse('연결 실패')