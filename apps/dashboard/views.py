from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings

from .models import Labour
from .helpers import *

import random

# Create your views here.
def login(request):
    return render(request, 'dashboard/login.html')

def signup(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        mobile_ = request.POST['mobile']
        password_ = request.POST['password']
        confirm_password_ = request.POST['confirm_password']

        if not is_email_verified:
            print("Invalid email")
            return redirect('signup')

        if Labour.objects.filter(email=email_).exists():
            print("Email already exist")
            return redirect('signup')
        
        if not is_valid_mobile_number(mobile_):
            print("Invalid mobile")
            return redirect('signup')
        
        if Labour.objects.filter(mobile=mobile_).exists():
            print("Mobile already exist")
            return redirect('signup')
        
        if password_ != confirm_password_:
            print("Password and confirm password does't match") 
            return redirect('signup')
        
        if not is_valid_password(password_)[0]:
            print(is_valid_password(password_)[1])
            return redirect('signup')
        
        print(make_password(password_), '------')
        new_labour = Labour.objects.create(
            email=email_,
            mobile=mobile_,
            password=make_password(password_)
        )
        new_labour.save()

        subject = "Email Conformation mail | Workbook"
        message = f"OTP: {random.randint(111111,999999)}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [f"{email_}"]
        send_mail(subject, message, from_email, recipient_list)
        
        print("Please check your mail for email confirmation. Your registraion has been successfully done.")
        return redirect('login')
        

        

    return render(request, 'dashboard/signup.html')

def forgot_password(request):
    return render(request, 'dashboard/forgot-password.html')

def otp_verify(request):
    return render(request, 'dashboard/otp-verify.html')

def index(request):
    return render(request, 'dashboard/index.html')