from django.contrib import admin
from .models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
     list_display = ('name', 'mainGenre', 'subGenre', 'trailerLink', 'image')
     search_fields = ('name', 'mainGenre', 'subGenre')
     list_filter  = ('mainGenre', 'subGenre')

class TvShowAdmin(admin.ModelAdmin):
     list_display = ('name', 'mainGenre', 'subGenre', 'trailerLink', 'image')
     search_fields = ('name', 'mainGenre', 'subGenre')
     list_filter  = ('mainGenre', 'subGenre')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'storeUrl', 'image', 'price', 'location')
    search_fields = ('name', 'description', 'price')
    list_filter = ('location',)
    ordering = ('name', 'price')
    prepopulated_fields = {'description': ('name',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(TvShow, TvShowAdmin)
admin.site.register(WishList, WishListAdmin)
