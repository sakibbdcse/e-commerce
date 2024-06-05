from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
# authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# forms models
from app_login.models import Profile
from app_login.forms import ProfileForms, SignUpForm
# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request, 'app_login/sign_up.html', context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Logged in')
            
    return render(request, 'app_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponse('logout success')