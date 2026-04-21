from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, default='Subaru')
    year = models.IntegerField()
    category = models.ForeignKey(
        Category,
        related_name='cars',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'car')

    def __str__(self):
        return f"{self.user} - {self.car}"
