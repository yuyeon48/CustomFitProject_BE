from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'disease', 'height', 'weight')

admin.site.register(UserProfile, UserProfileAdmin)

