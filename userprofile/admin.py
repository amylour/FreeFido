from django.contrib import admin
from .models import AccountProfile


@admin.register(AccountProfile)
class AccountProfileAdmin(admin.ModelAdmin):
    list_display = (
        'profile_pic',
        'first_name',
        'last_name',
        'phone')
    list_filter = ('last_name', 'phone')
    search_fields = ['first_nane', 'last_name', 'phone']
