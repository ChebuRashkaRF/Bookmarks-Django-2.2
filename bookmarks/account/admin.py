from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профили"""

    list_display = ['user', 'date_of_birth', 'photo']
