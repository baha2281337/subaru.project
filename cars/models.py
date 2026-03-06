from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)        
    year = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    is_available = models.BooleanField(default=True)  
    name = models.CharField(max_length=100, default="Subaru")  

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name