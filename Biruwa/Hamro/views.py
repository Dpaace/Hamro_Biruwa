from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate , get_user_model , logout
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/homepage')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'login.html')   