from datetime import datetime
from distutils.command.upload import upload
from django.db import models            
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    phone_number = models.CharField(max_length=15,null=True)
    
class Gallery(models.Model):
    photo_title = models.CharField(max_length=285)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    created_date = models.DateTimeField(default=datetime.now, blank=True)



