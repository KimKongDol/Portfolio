# render는 index.html을 전송하는 함수
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# render는 템플릿을 불러오고 rediredt는 URL로 이동시켜줌


def showmain(request):
    return render(request, 'index.html')


def showgallery(request):
    return render(request, 'gallery.html')


def showcontact(request):
    return render(request, 'contact.html')
