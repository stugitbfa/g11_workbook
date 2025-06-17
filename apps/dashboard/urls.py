from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('otp-verify/', otp_verify, name='otp_verify'),
    path('dashboard/', index, name='index')
]