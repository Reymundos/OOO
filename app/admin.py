from django.contrib import admin
from .models import Shopping
# Register your models here.


@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'amount', 'time')
    list_display_links = ('user', 'title')
