from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('', index, name='index'),
]