from django.forms.forms import Form
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , logout
from django.contrib.auth.models import auth, User
from Hamro.models import Gallery, News, Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from . import models
from product import models
# from product import models
from Hamro.forms import UserResgistrationForm
from Hamro.models import AuthUser
from django.core.mail import send_mail

User = get_user_model()

#Create your views here.


from product.models import Product

# Create your views here.


def home(request):
    # For showing featured Products
    featured_product = Product.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'featured_product': featured_product,
    }
    return render(request, 'pages/home.html',data)

def register(request):
    form = UserResgistrationForm()
    if request.method =='POST':
        form = UserResgistrationForm(request.POST)
        if form.is_valid():
            print("here")
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get('phone_number')
            user = User.objects.create_user(
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                phone_number=phone_number,
                                password=password)
            user.save()

    context = {
        "form": form 
    }
    return render(request, 'pages/registration.html')
 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Hamro:home')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('Hamro:login')
    else:  
        return render(request, 'pages/login.html')   


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['biruwahamro@gmail.com' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'pages/contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'pages/contact.html' , {})      

def blog(request):
    blog = Blog.objects.order_by('-created_date')
    paginator = Paginator(blog, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'blog': paged_product,
    }
    return render(request, 'pages/blog.html', data)

def blog_detail(request, id):
    single_blog = get_object_or_404(Blog, pk=id)

    data = {
        'single_blog': single_blog,
    }

    return render(request, 'pages/blog_detail.html', data)

def gallery(request):
    gallery = Gallery.objects.all()
    data = {
        'gallery': gallery,
    }
    return render(request, 'pages/gallery.html', data)

def news(request):
    news = News.objects.order_by('-created_date')
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)
    data = {
        'news': paged_news,
    }
    return render(request, 'pages/news.html', data)


def logout(request):
    auth.logout(request)
    return redirect('Hamro:home')

def dashboard(request):
    return render(request, 'pages/dashboard.html')