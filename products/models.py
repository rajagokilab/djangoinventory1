from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
