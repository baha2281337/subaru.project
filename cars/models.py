from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)        
    year = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    is_available = models.BooleanField(default=True)  
    name = models.CharField(max_length=100, default="Subaru")  
    from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
