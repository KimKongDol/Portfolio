from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    # path('gallery/', showgallery, name='gallery'),
    # path('contact/', showcontact, name='contact'),
    path('music_index/', music_index, name='music_index'),
    # 하나의 템플릿으로 여러 경우의 페이지를 띄운다.
    path('<str:id>', detail, name='detail'),
    path('music_new/', new, name='new'),
    path('music_create/', create, name="create"),
    path('music_edit/<str:id>', edit, name="edit"),
    path('music_update/<str:id>', update, name="update"),
    path('music_delete/<str:id>', delete, name="delete"),
]
