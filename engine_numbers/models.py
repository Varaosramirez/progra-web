# engine_numbers/models.py
from django.db import models

class EngineNumber(models.Model):
    number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.number
