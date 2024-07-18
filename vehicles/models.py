# vehicles/models.py
from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)  # Permitir null y blank temporalmente

    def __str__(self):
        return self.model
