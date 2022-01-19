from django.urls import path
from django.contrib import admin
from Hamro import views
from django.contrib.auth import views as auth_views 

app_name = "Hamro"

urlpatterns = [
    path('', views.home, name='home'),
    path("register/",views.register, name='register'),
    path("login/", views.login, name='login'),
    path("homepage/", views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),

]
