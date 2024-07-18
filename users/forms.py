from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label='¿Es Administrador?')
    security_code = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput, label='Código de Seguridad')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'security_code')

    def clean(self):
        cleaned_data = super().clean()
        is_admin = cleaned_data.get('is_admin')
        security_code = cleaned_data.get('security_code')
        if is_admin and security_code != 'Alfredonx1@':  # Reemplaza 'Alfredonx1@' con tu código de seguridad
            self.add_error('security_code', 'Código de seguridad incorrecto.')
        return cleaned_data

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone']