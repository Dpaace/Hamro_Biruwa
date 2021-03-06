from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.product, name='product'),
    path('<int:id>', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view, name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),

    path('customer-address', views.customer_address_view, name='customer-address'),
    path('payment-success/<int:user_id>', views.payment_success_view,name='payment-success'),
    path('submit_review/<int:product_ids>', views.submit_review, name='submit_review'),
]
