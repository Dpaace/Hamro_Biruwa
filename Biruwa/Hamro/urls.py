from django.urls import path
from django.contrib import admin
from Hamro import views
from django.contrib.auth import views as auth_views 

app_name = "Hamro"

urlpatterns = [
    path('', views.home, name='home'),
    path("register/",views.register, name='register'),
    path("login/", views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('<int:id>', views.blog_detail, name='blog_detail'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("logout/", views.logout, name='logout'),

    # path('password_reset/',
    # auth_views.PasswordResetView.as_view(template_name='pages/accounts/password_reset_form.html'),
    # name='password_reset'),

    # path('password_reset/done/',
    # auth_views.PasswordResetDoneView.as_view(template_name='pages/accounts/password_reset_done.html'),
    # name='password_reset_done'),

    # path('reset/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(template_name='pages/accounts/password_reset_confirm.html'),
    # name='password_reset_confirm'),

    # path('reset/done/',
    # auth_views.PasswordResetCompleteView.as_view(template_name='pages/accounts/password_reset_complete.html'),
    # name='password_reset_complete'),
    
]
