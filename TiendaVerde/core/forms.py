from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", "email", "password1", "password2"]
        help_texts = { k : "" for k in fields}

    def clean_user(self):
        username = self.cleaned_data.get('username')
        if not user:
            raise forms.ValidationError("El usuario es obligatorio")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coiciden.")
        return password2


