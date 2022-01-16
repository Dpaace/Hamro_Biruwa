from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate , get_user_model , logout
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')