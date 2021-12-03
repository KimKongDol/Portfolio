from django.urls import path
from .views import *

app_name = "error"
urlpatterns = [
    path('error_index/', error_index, name="error_index"),
    path('error_detail/<str:id>', error_detail, name="error_detail"),
    path('error_new/', error_new, name="new"),
    path('error_create/', error_create, name="create"),
    path('error_edit/<str:id>', error_edit, name="error_edit"),
    path('error_update/<str:id>', error_update, name="update"),
    path('error_delete/<str:id>', error_delete, name="error_delete"),
]
