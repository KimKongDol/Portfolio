from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    # path('gallery/', showgallery, name='gallery'),
    # path('contact/', showcontact, name='contact'),
    path('music_index/', music_index, name='music_index'),
    # 하나의 템플릿으로 여러 경우의 페이지를 띄운다.
    path('<str:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name="create"),
]
