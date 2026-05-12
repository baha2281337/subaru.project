from django.contrib import admin

from .models import Car, Category, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'car')
