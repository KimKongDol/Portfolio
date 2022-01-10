from django.urls import path
from .views import *  # 'index'라는 app에서 views.py의 함수들을 들고 온다.
app_name = "users"
urlpatterns = [
    path('mypage/', mypage, name='mypage'),  # views에 있는 showmain함수 실행
]
