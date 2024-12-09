from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>', post,  name='post'),
]