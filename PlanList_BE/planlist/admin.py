from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'storeUrl', 'image', 'price', 'location')
    search_fields = ('name', 'description', 'price')
    list_filter = ('location',)
    ordering = ('name', 'price')
    prepopulated_fields = {'description': ('name',)}

admin.site.register(Books, BookAdmin)
admin.site.register(WishList, WishListAdmin)
