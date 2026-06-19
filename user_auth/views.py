from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Custom_User
from .utils import generate_otp, send_otp_email

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_email_verified==True:
                login(request, user)
                messages.success(request, f'Login Successful! Welcome back {username.upper()}')
                return redirect('home')
            else:
                otp=generate_otp()
                user.email_otp=otp
                user.save()
                send_otp_email(request, username, user.email, otp)
                context={'email':user.email}
                messages.success(request, "Please verify your email!")
                return redirect('verify_email')
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
        context={'username':username, 'email':email}
        if Custom_User.objects.filter(username=username).exists():
            messages.error(request, "This username has already been used. Please choose a different username.")
            return render(request, 'registration.html', context)
        if Custom_User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists. Please use a different email address.")
            return render(request, 'registration.html', context)
        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please enter same password for PASSWORD FIELD AND CONFIRM PASSWORD FIELD')
            return render(request, 'registration.html', context)
        if not username or not email or not password or not confirm_password:
            messages.error(request, "Username, email and password are required.")
            return render(request, 'registration.html')
        otp=generate_otp()
        Custom_User.objects.create_user(
            username=username,
            email=email,
            password=password,
            email_otp=otp
            )
        send_otp_email(request, username, email, otp)
        messages.success(request, 'Account Created! Check your email account for an email.')
        return redirect('verify_email')
    else:
        return render(request, 'registration.html')

def verify_email(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email')
        otp=request.POST.get('otp')
        context={'email':email}
        
        if Custom_User.objects.filter(email=email).exists():
            user=Custom_User.objects.get(email=email)
            if user.is_email_verified==True:
                messages.success(request, "Account is already verified.")
                return redirect('login')

            # try:
            #     otp=int(otp)
            # except ValueError as e:
            #     messages.error(request, "OTP must be numbers!")
            #     return render(request, 'verify_email.html', context)
            
            if user.email_otp==otp:
                user.is_email_verified=True
                user.email_otp=None
                user.save()
                messages.success(request, "Account verified. You can login now")
                return redirect('login')
            else:
                messages.error(request, "Wrong OTP !")
                return render(request, 'verify_email.html', context)
        else:
            messages.error(request, 'User does not exists!')
            return redirect('register')
    else:   
        return render(request, 'verify_email.html')

def user_logout(request):
    logout(request)
    return redirect('home')