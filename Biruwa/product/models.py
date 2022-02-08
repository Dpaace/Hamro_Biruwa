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

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

class ReviewRating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    subject=models.CharField(max_length=100, blank=True)
    review=models.TextField(max_length=500,blank=True)
    ip =models.CharField(max_length=20,blank=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject   