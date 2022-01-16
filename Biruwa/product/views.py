import imp
from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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