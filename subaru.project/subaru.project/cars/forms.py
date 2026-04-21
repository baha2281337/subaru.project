from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["name", "description", "price", "year", "is_available", "category", "image"]
