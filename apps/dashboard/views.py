from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings

from functools import wraps

from .models import Labour
from .helpers import *

import random

# Create your views here.


def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'labour_id' not in request.session:
            return redirect('login')  # redirect to login page
        return view_func(request, *args, **kwargs)
    return wrapper


def login(request):
    if request.method == 'POST':
        email_ = request.POST['email'] 
        password_ = request.POST['password'] 

        if not Labour.objects.filter(email=email_).exists():
            print("Email does't exist")
            return redirect('login')
        
        get_labour = Labour.objects.get(email=email_)

        if not get_labour.is_active:
            print("Your account is deactive please contact to customer care")
            return redirect('login')
        is_password_verify = check_password(password_, get_labour.password)
        if not is_password_verify:
            print("Email or password not match")
            return redirect('login') 
        
        request.session['labour_id'] = str(get_labour.wid)
        return redirect('index')


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

        otp = random.randint(111111,999999)

        subject = "Email Conformation mail | Workbook"
        message = f"""
        Hello Labour,

        Thank you for registering with Workbook.

        Your One-Time Password (OTP) for email verification is: {otp}

        Please enter this OTP to complete your registration. 

        If you did not initiate this request, please ignore this email.

        Best regards,  
        Workbook Team
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [f"{email_}"]
        send_mail(subject, message, from_email, recipient_list)
        new_labour.otp = otp
        new_labour.save()
        print("Please check your mail for email confirmation. Your registraion has been successfully done.")
        context = {
            'email': email_
        }
        return render(request, 'dashboard/email_verify.html', context)
        

        

    return render(request, 'dashboard/signup.html')

def forgot_password(request):
    return render(request, 'dashboard/forgot-password.html')

def email_verify(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']

        get_labour = Labour.objects.get(email=email_)

        if otp_ != get_labour.otp:
            print("Invalid OTP")
            context = {
            'email': email_
            }
            return render(request, 'dashboard/email_verify.html', context)

        get_labour.is_active = True
        get_labour.save()
        return redirect('login')

    return render(request, 'dashboard/email_verify.html')

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def logout(request):
    del request.session['labour_id']
    print("Now, you are logged Out")
    return redirect('login')
    