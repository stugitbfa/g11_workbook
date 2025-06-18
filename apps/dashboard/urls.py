from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('email-verify/', email_verify, name='email_verify'),
    path('dashboard/', index, name='index'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]