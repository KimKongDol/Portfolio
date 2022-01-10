from django.urls import path
from .views import *  # 'index'라는 app에서 views.py의 함수들을 들고 온다.

app_name = "gallery"
urlpatterns = [
    # path('', showmain, name='index'),  # views에 있는 showmain함수 실행
    path('gallery_index/', gallery_index, name='gallery_index'),
    path('gallery_index/christmas', christmas, name='christmas'),
]
