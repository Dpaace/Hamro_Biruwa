import imp
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from .models import Product
from Hamro.models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth

# Create your views here.
def product(request):
    product = Product.objects.order_by('-created_date')
    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'product': paged_product,
    }
    return render(request, 'product/product.html', data)

def product_detail(request, id):
    single_product = get_object_or_404(Product, pk=id)

    data = {
        'single_product': single_product,
    }

    return render(request, 'product/product_detail.html', data)

# def cart(request):
#     return render(request, 'product/cart.html')

def add_to_cart_view(request, pk):
    products = models.Product.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
        
    else:
        product_count_in_cart=1

    
    response = render(request, 'product/product.html',{'products':products,'product_count_in_cart':product_count_in_cart})
    
    # adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product=models.Product.objects.get(id=pk)
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
            
        response.set_cookie('product_ids', product_ids)
        
    else:
        response.set_cookie('product_ids', pk)  
        
    
    product=models.Product.objects.get(id=pk)
    messages.success(request, product.product_title + ' added to cart successfully!')
    return response
    
    

# for checkout of cart
def cart_view(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)

    
    return render(request,'product/cart.html', {'products':products,'total':total,'product_count_in_cart':product_count_in_cart})

def remove_from_cart_view(request,pk):
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        # for p in products:
        #     total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'product/cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response


# For Searching Products
def search(request):
    product = Product.objects.order_by('-created_date')
    blog = Blog.objects.order_by('-created_date')

    product_search = Product.objects.values_list('product_title', flat=True).distinct()
    blog_search = Blog.objects.values_list('blog_title', flat=True).distinct()

    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = product.filter(description__icontains=keyword)

    if 'product_title' in request.GET:
        product_title = request.GET['product_title']
        if product_title:
            product = product.filter(model__iexact=product_title)
    
    if 'blog_title' in request.GET:
        blog_title = request.GET['blog_title']
        if Blog.objects.order_by('-created_date'):
            blog = blog.filter(model__iexact=blog_title)

    data = {
        'product': product,
        'product_search': product_search,
        'blog_search':blog_search,
        
    }
    return render(request, 'product/search.html', data)
