# cart/models.py
from django.db import models
from vehicles.models import Vehicle
from django.conf import settings

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.vehicle.model} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, related_name='carts', blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Carrito de {self.user.username}"