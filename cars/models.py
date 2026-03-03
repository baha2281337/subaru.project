from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.title