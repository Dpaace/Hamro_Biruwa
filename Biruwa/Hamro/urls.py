from django.urls import path
from django.contrib import admin
from Hamro import views
from django.contrib.auth import views as auth_views 

app_name = "Hamro"

urlpatterns = [
    path('', views.home, name='home'),
    path("register/",views.register, name='register'),
    path('login', views.login_fn, name='login'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('<int:id>', views.blog_detail, name='blog_detail'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("logout/", views.logout, name='logout'),

    path('deleteuser/<int:user_id>', views.delete_user, name='delete_user'),

    path("password_reset", views.password_reset_request, name="password_reset"),
    
    # User Related Views
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
]
