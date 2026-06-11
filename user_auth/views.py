from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages

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
    
    return render(request, 'registration.html')

def verify_email(request):
    return render(request, 'verify_email.html')

def user_logout(request):
    logout(request)
    return redirect('home')