from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate , get_user_model , logout
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages

from product.models import Product

# Create your views here.
def home(request):
    featured_product = Product.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'featured_product': featured_product,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')