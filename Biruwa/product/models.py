from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


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
