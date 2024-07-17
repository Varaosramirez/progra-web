# sales/models.py
from django.db import models
from vehicles.models import Vehicle
from employees.models import Employee

class Sale(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Sale of {self.vehicle} to {self.customer_name} on {self.date}"
