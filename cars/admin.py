from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "price", "is_available")
    list_filter = ("is_available", "year")
    search_fields = ("title", "description")