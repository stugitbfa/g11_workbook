from django.urls import path
# from .views import *
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.show, name='show'),
    path('insert/', views.insert, name='insert'),
    path('update-post/<int:post_id>', views.update_post, name='update_post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete_post'),
]