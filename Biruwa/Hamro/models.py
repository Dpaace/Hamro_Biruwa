from django.db import models            
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    phone_number = models.CharField(max_length=15,null=True)
    



