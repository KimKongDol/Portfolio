from django.urls import path
from .views import *  # 'index'라는 app에서 views.py의 함수들을 들고 온다.

app_name = "gallery"
urlpatterns = [
    # path('', showmain, name='index'),  # views에 있는 showmain함수 실행
    path('gallery_index/', gallery_index, name='gallery_index'),
    path('gallery_index/christmas', christmas, name='christmas'),
    path('gallery_index/caesar', caesar, name='caesar'),

    path('input_string/', input_string, name="input_string"),
    path('random_string/', random_string ,name="random_string"),
    path('test', test ,name="test"),
    # path('caesar_encryp/', caesar_encryp,name="caesar_encryp"),
]
