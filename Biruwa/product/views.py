import imp
from django.shortcuts import get_object_or_404, redirect, render
from product import forms,models
from .models import Product, ReviewRating
from Hamro.models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from Hamro import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import login_required
User = get_user_model()
from .forms import ReviewForm

# Create your views here.
def product(request):
    product = Product.objects.order_by('-created_date')
    paginator = Paginator(product, 2)
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




def add_to_cart_view(request, pk):
    products = models.Product.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
        
    else:
        product_count_in_cart=1
    data= {
        'products':products,
        'product_count_in_cart':product_count_in_cart
    }
    
    response = render(request, 'product/product.html', data)
    
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
    
    

# # for checkout of cart
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
        
    data = {
        'products':products,
        'total':total,
        'product_count_in_cart':product_count_in_cart
    }
    
    return render(request,'product/cart.html', data)

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
    product_search = Product.objects.values_list('product_title', flat=True).distinct()

    # description__icontains
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = product.filter(description__icontains=keyword)

    if 'product_title' in request.GET:
        product_title = request.GET['product_title']
        if product_title:
            product = product.filter(model__iexact=product_title)
    


    data = {
        'product': product,
        'product_search': product_search, 
    }
    return render(request, 'product/search.html', data)

@login_required(login_url='Hamro:login')
def customer_address_view(request):
    product_in_cart=False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart=True

    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            #for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total=0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart=product_ids.split('|')
                    products=models.Product.objects.all().filter(id__in = product_id_in_cart)
                    for p in products:
                        total=total+p.price

            response = render(request, 'product/payment.html',{'total':total})
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            return response
    return render(request,'product/customer_address.html',{'addressForm':addressForm,'product_in_cart':product_in_cart,'product_count_in_cart':product_count_in_cart})

def payment_success_view(request, user_id):
    user = User.objects.get(id=user_id)
    products=None
    email=None
    mobile=None
    address=None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email=request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile=request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address=request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for product in products:
        models.Orders.objects.get_or_create(customer=user,product=product,status='Pending',email=email,mobile=mobile,address=address)

    # after order placed cookies should be deleted
    response = render(request,'product/payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response

def submit_review(request, product_ids):
    url =request.META.get('HTTP_REFERER')
    if request.method =="POST":
        try:
            reviews=ReviewRating.objects.get(id=request.user.id, product__id=product_ids)
            form =ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request, 'Thankyou! Your review has been updated.')
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form =ReviewForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.review=form.cleaned_data['review']
                data.ip=request.META.get('REMOTE_ADDR')
                data.product_ids=product_ids
                data.user_id =request.user.id
                data.save()
                # messages.success(request, 'Thankyou! Your review has been submited.')
                return redirect(url)




