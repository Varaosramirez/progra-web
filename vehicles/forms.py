# vehicles/forms.py
from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'description', 'price', 'image']  # Añade 'brand' si lo necesitas
