from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from product.views import product, product_detail, search, add_to_cart_view, cart_view
from product.views import remove_from_cart_view,customer_address_view, payment_success_view
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class TestUrls(SimpleTestCase):
    def test_case_product_url(self):
        url=reverse("product")
        print(resolve(url))
        self.assertEquals(resolve(url).func,product)

    def test_case_product_detail_url(self):
        url=reverse("product_detail")
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_detail)

    def test_case_search_url(self):
        url=reverse("search")
        print(resolve(url))
        self.assertEquals(resolve(url).func,search)

    def test_case_add_to_cart_url(self):
        url=reverse("add-to-cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,add_to_cart_view)

    def test_case_cart_view_url(self):
        url=reverse("cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,cart_view)

    def test_case_remove_from_cart_url(self):
        url=reverse("remove-from-cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,remove_from_cart_view)

    def test_case_customer_address_url(self):
        url=reverse("customer-address")
        print(resolve(url))
        self.assertEquals(resolve(url).func,customer_address_view)

    def test_case_payment_url(self):
        url=reverse("payment-success")
        print(resolve(url))
        self.assertEquals(resolve(url).func,payment_success_view)
    

    

    

    









