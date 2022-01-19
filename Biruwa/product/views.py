import imp
from django.shortcuts import get_object_or_404, render
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

def product_detail(request, id):
    single_product = get_object_or_404(Product, pk=id)

    data = {
        'single_product': single_product,
    }

    return render(request, 'product/product_detail.html', data)
