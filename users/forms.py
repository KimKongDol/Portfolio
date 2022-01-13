from django import forms
from .models import User
import django
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'relation', 'home',
                  'how', 'email', 'password1', 'password2']

    def clean(self):
        username = self.cleaned_data.get('username')
        if username:
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError("이미 존재하는 별명입니다.")
        return username
