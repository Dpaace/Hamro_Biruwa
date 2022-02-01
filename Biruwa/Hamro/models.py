from datetime import datetime
from distutils.command.upload import upload
from django.db import models            
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    phone_number = models.CharField(max_length=15,null=True)


class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.blog_title
    
class Gallery(models.Model):
    photo_title = models.CharField(max_length=285)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_title_1 = models.CharField(max_length=100, default='SOME STRING')
    description = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
