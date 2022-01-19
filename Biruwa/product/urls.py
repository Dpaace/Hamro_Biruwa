from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.product, name='product'),
    path('<int:id>', views.product_detail, name='product_detail')
]
