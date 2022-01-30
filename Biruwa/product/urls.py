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
]
