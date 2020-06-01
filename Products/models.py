from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
