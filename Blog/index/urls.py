# 인덱스 앱에 대한 페이지들 url 관리

from django.urls import path
from .views import *  # 'index'라는 app에서 views.py의 함수들을 들고 온다.

app_name = "index"
urlpatterns = [
    path('', showmain, name='index'),  # views에 있는 showmain함수 실행
    path('gallery/', showgallery, name='gallery'),
    path('contact/', showcontact, name='contact'),
    # path('about/', showabout, name='music'),
    # # 하나의 템플릿으로 여러 경우의 페이지를 띄운다.
    # path('<str:id>', detail, name='detail'),
    # path('new/', new, name='new'),
    # path('create/', create, name="create"),
]
