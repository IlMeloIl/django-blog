from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>', post,  name='post'),
    path('create/', create_post, name='create_post'),
    path('post/<slug:slug>/edit', edit_post, name='edit_post'),
    path('post/<slug:slug>/delete', delete_post, name='delete_post'),
]