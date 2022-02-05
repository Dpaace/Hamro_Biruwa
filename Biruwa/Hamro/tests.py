from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from Hamro.views import home, register, login_fn, contact, logout,about, delete_user, gallery, news
from Hamro.views import dashboard, password_reset_request, edit_profile_view, blog, blog_detail
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse("Hamro:home")
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_case_register_url(self):
        url=reverse("Hamro:register")
        print(resolve(url))
        self.assertEquals(resolve(url).func,register)

    def test_case_login_url(self):
        url=reverse("Hamro:login")
        print(resolve(url))
        self.assertEquals(resolve(url).func,login_fn)

    def test_case_home_url(self):
        url=reverse("Hamro:contact")
        print(resolve(url))
        self.assertEquals(resolve(url).func,contact)

    def test_case_about_url(self):
        url=reverse("Hamro:about")
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)

    def test_case_blog_url(self):
        url=reverse("Hamro:blog")
        print(resolve(url))
        self.assertEquals(resolve(url).func,blog)

    # def test_case_blog_detail_url(self):
    #     url=reverse("Hamro:blog_detail")
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,blog_detail)

    def test_case_news_url(self):
        url=reverse("Hamro:news")
        print(resolve(url))
        self.assertEquals(resolve(url).func,news)

    # def test_case_delete_user_url(self):
    #     url=reverse("Hamro:delete_user")
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,delete_user)

    def test_case_logout_url(self):
        url=reverse("Hamro:logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,logout)
    
    def test_case_gallery_url(self):
        url=reverse("Hamro:gallery")
        print(resolve(url))
        self.assertEquals(resolve(url).func,gallery)
    
    def test_case_dashboard_url(self):
        url=reverse("Hamro:dashboard")
        print(resolve(url))
        self.assertEquals(resolve(url).func,dashboard)

    def test_case_password_reset_request_url(self):
        url=reverse("Hamro:password_reset")
        print(resolve(url))
        self.assertEquals(resolve(url).func,password_reset_request)

    def test_case_edit_profile_view_url(self):
        url=reverse("Hamro:edit-profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func,edit_profile_view)
    

    

    







