from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return f"{self.title} ({self.year})"