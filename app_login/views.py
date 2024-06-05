from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from app_login.models import Profile
from app_login.forms import ProfileForms, SignUpForm

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'app_login/sign_up.html', context={'form': form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', reverse('profile'))
                return HttpResponseRedirect(next_url)
    return render(request, 'app_login/login.html', context={'form': form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForms(instance=profile)
    if request.method == 'POST':
        form = ProfileForms(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            form = ProfileForms(instance=profile)
    return render(request, 'app_login/change_profile.html', context={'form': form})
