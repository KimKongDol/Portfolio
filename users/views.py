from django.shortcuts import render, redirect  # render템플릿,redirect는 url
from django.views.generic import CreateView
from users.models import User
from django.contrib import auth, messages
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def mypage(request):
    return render(request, 'mypage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # return redirect('/mypage')  # 로그인 성공시 마이페이지로 이동
            messages.success(request, "회원가입을 환영합니다.")
        return redirect('/mypage')  # 로그인 성공시 페이지 이동

    else:
        form = SignupForm()
    return render(request, 'signup2.html', {'form': form})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요!'

        else:
            user = User.objects.get(username=username)

            if check_password(password, member.password):
                pass
                # session!
                # redirect!

            else:
                res_data['error'] = '비밀번호가 다릅니다!'

        return render(request, 'login.html', res_data)
