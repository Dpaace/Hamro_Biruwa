from django.contrib import admin
from .models import Product, Orders, ReviewRating
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.product_photo.url))

    thumbnail.short_description = 'Product_Image'

    list_display = ('id','thumbnail','product_title', 'price', 'is_featured', 'is_material','is_medicine','available')
    list_display_links = ('id', 'thumbnail', 'product_title')
    list_editable = ('is_featured', 'is_material','is_medicine','available')
    search_fields = ('product_title',)
    list_filter = ('product_title', 'price')

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.product.product_photo.url))

    thumbnail.short_description = 'Product_Image'

    list_display = ('id','thumbnail','customer', 'product', 'email', 'address','mobile','order_date','status')
    list_display_links = ('id', 'thumbnail')
    list_editable = ('status',)
    search_fields = ('customer',)
    list_filter = ('email', 'mobile')


admin.site.register(Orders, OrderAdmin)


admin.site.register(ReviewRating)

