from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method =='GET':
        form = SignUpForm
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    
    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')