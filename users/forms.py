from django import forms
from .models import User
import django
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'relation', 'home',
                  'how', 'email', 'password1', 'password2']