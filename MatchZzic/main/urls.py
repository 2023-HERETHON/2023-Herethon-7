from django.urls import path
from . import views
from main.views import main

urlpatterns = [
    path('main/', main, name='main'),
]