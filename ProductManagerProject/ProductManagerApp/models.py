from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name
