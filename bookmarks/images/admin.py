from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Изображения"""

    list_display = ['title', 'id', 'slug', 'image', 'created']
    list_filter = ['created']
