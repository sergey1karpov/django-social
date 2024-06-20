from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

from user_profile.models import UserProfile


def registration(request):
    if request.method == 'GET':
        return render(request, 'auth_module/actions/register.html')

    if request.method == 'POST':

        if ifEmailAlreadyExists(request.POST.get('email')):
            raise ValidationError("Email already exists")

        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
        )

        UserProfile.objects.create(user=user)

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(reverse('blogger:main_page'), user=user)


def login_user(request):
    if request.method == 'GET':
        return render(request, 'auth_module/actions/login.html')

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if not user:
            raise Http404("User not found")
        else:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('blogger:main_page'), user=user)


def logout_view(request):
    logout(request)
    return redirect(reverse('blogger:main_page'))


def ifEmailAlreadyExists(email:str) -> bool:
    if User.objects.filter(email=email).exists():
            return True
    return False
