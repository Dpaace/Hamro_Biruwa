import imp
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from product.views import product, product_detail, search, add_to_cart_view, cart_view
from product.views import remove_from_cart_view,customer_address_view, payment_success_view, submit_review
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Hamro.views import *

# Create your tests here.

User = get_user_model()


class TestUrls(SimpleTestCase):
    def test_case_product_url(self):
        url=reverse("product")
        print(resolve(url))
        self.assertEquals(resolve(url).func,product)

    def test_case_product_detail_url(self):
        url=reverse("product_detail", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_detail)

    def test_case_search_url(self):
        url=reverse("search")
        print(resolve(url))
        self.assertEquals(resolve(url).func,search)

    def test_case_add_to_cart_url(self):
        url=reverse("add-to-cart" , args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,add_to_cart_view)

    def test_case_cart_view_url(self):
        url=reverse("cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,cart_view)

    def test_case_remove_from_cart_url(self):
        url=reverse("remove-from-cart" , args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,remove_from_cart_view)

    def test_case_customer_address_url(self):
        url=reverse("customer-address")
        print(resolve(url))
        self.assertEquals(resolve(url).func,customer_address_view)

    def test_case_payment_url(self):
        url=reverse("payment-success" , args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,payment_success_view)

    def test_case_submit_review_url(self):
        url=reverse("submit_review" , args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,submit_review)

    
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_product_views(self):
        response=self.client.get(reverse('product'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'product/product.html')
    
    def test_cart_views(self):
        response=self.client.get(reverse('cart'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'product/cart.html')

    def test_search_views(self):
        response=self.client.get(reverse('search'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'product/search.html')

    def test_blog_views(self):
        response=self.client.get(reverse('Hamro:blog'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'pages/blog.html')

    def test_gallery_views(self):
        response=self.client.get(reverse('Hamro:gallery'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'pages/gallery.html')

    

    

    









