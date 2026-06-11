from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import Custom_User


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Login Successful! Welcome back {username.upper()}')
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if Custom_User.objects.filter(username=username).exists():
            messages.error('Username must be unique and can contain letters, numbers, and underscores.')
            return render(request, 'registration.html')
        if Custom_User.objects.filter(email=email).exists():
            messages.error('Email must be unique.')
            return render(request, 'registration.html')
        if password != confirm_password:
            messages.error('Passwords do not match. Please enter same password for PASSWORD FIELD AND CONFIRM PASSWORD FIELD')
            return render(request, 'registration.html')
        if not username or not email or not password or not confirm_password:
            messages.error("Username, email and password are required.")
            return render(request, 'registration.html')
        Custom_User.objects.create_user(
            username=username,
            email=email,
            password=password,
            )
        messages.success('Account Created! Login with your credential')
        redirect('login')
    else:
        return render(request, 'registration.html')

def verify_email(request):
    return render(request, 'verify_email.html')

def user_logout(request):
    logout(request)
    return redirect('home')