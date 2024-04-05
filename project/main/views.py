from django.shortcuts import render, redirect # render : 템플릿을 불러옴 / redirect : URL로 연결
from django.utils import timezone #Django에서 제공하는 시간 관련 유틸리티 모듈

from .models import Blog

# Create your views here.
def mainpage(request):
    context = {
        'generation': 12,
        'members': ['현아', '영심이', '티준'],
        'info':{'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'}
    }
    return render(request, 'main/mainpage.html', context)
def secondpage(request):
    return render(request, 'main/secondpage.html')
def new_blog(request):
    return render(request, 'main/new-blog.html')

# 데이터베이스에 저장하는 함수
def create(request):
    new_blog = Blog()
    
    # POST로 들어오는 데이터를 new_blog 객체에 저장
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()

    # new_blog 객체를 저장
    new_blog.save()

    return redirect('datail', new_blog.id)
