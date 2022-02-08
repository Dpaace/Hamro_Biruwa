from django.contrib import admin
from .models import Product, Orders
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.product_photo.url))

    thumbnail.short_description = 'Product_Image'

    list_display = ('id','thumbnail','product_title', 'price', 'is_featured', 'is_material','is_medicine')
    list_display_links = ('id', 'thumbnail', 'product_title')
    list_editable = ('is_featured', 'is_material','is_medicine')
    search_fields = ('product_title',)
    list_filter = ('product_title', 'price')

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)




