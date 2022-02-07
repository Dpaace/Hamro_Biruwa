from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 

User = get_user_model()
# Create your models here.
class Product(models.Model):
    product_title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    product_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    is_material = models.BooleanField(default=False)
    is_medicine = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_title

class Cart(models.Model):
    cart_id      = models.CharField(max_length=250, blank=True)
    date_added   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product
