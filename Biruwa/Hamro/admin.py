from django.contrib import admin
from Hamro.models import Gallery, News
from django.utils.html import format_html

from Hamro.models import AuthUser

# Register your models here.

admin.site.register(AuthUser)

class GalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'Gallery_Image'

    list_display = ('id','thumbnail','photo_title')
    list_display_links = ('id', 'thumbnail')

admin.site.register(Gallery, GalleryAdmin)

class NewsAdmin(admin.ModelAdmin):

    list_display = ('id', 'news_title')
    list_display_links = ('id', 'news_title')
admin.site.register(News, NewsAdmin)