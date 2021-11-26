from django.urls import path
from .views import *

app_name = "error"
urlpatterns = [
    path('error_index/', error_index, name="error_index"),
]
