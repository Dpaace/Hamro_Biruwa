from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , logout, login
from django.contrib.auth.models import auth, User
from . import forms, models
from Hamro.models import Gallery, News, Blog, Brand
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models


# from product import models
from Hamro.forms import UserResgistrationForm
from django.core.mail import send_mail

User = get_user_model()

#Create your views here.


from product.models import Product, Orders

# For reset password
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def home(request):
    # For showing featured Products
    featured_product = Product.objects.order_by('-created_date').filter(is_featured=True)
    material_product = Product.objects.order_by('-created_date').filter(is_material=True)
    medicine_product = Product.objects.order_by('-created_date').filter(is_medicine=True)
    brand_photo = Brand.objects.all()
    data = {
        'featured_product': featured_product,
        'material_product': material_product,
        'medicine_product': medicine_product,
        'brand_photo': brand_photo,
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
            return redirect('Hamro:login')
    context = {
        "form": form 
    }
    return render(request, 'pages/registration.html')
 
def login_fn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('username')
            print(request.user.username)

            return redirect('Hamro:home')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('Hamro:login')
    else:  
        return render(request, 'pages/login.html')   


def about(request):
    return render(request, 'pages/about.html')

def help(request):
    return render(request, 'pages/help.html')

def discussion(request):
    return render(request, 'pages/discussion.html')

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
    paginator = Paginator(blog, 1)
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
    # messages.success(request, "Sucessfully Logged Out")
    return redirect('Hamro:home')



def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User is deleted successfully')
    return redirect('Hamro:login')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "pages/accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'biruwahamro@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="pages/accounts/password_reset_form.html", context={"password_reset_form":password_reset_form})


@login_required(login_url='Hamro:login')
def dashboard(request):
    return render(request, 'pages/dashboard.html')

@login_required(login_url='Hamro:login')
def edit_profile_view(request):
    user=User.objects.get(id=request.user.id)
    userForm=forms.UserResgistrationForm(instance=user)
    mydict={
        'UserResgistrationForm':UserResgistrationForm,
        'user':user
    }
    if request.method=='POST':
        userForm=forms.UserResgistrationForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            user.set_password(user.password)
            userForm.save()
            # user.set_password(user.password)
            # user.save()
            return HttpResponseRedirect('dashboard')
    return render(request,'pages/edit_profile.html',context=mydict)


@login_required(login_url='Hamro:login')
def myorder_view(request):
    order = Orders.objects.all()
    data = {
        'order':order,
    }
    return render(request,'pages/myorder.html', data)

