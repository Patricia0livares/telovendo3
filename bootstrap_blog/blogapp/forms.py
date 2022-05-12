from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields


class RegistroClienteForm(forms.Form):
    nombre=forms.CharField (max_length=50, required=True)
    apellido=forms.CharField (max_length=50, required=True)
    apellidoM=forms.CharField (max_length=50, required=True)
    correo=forms.CharField(widget=forms.EmailInput)
    pais=forms.CharField(max_length=50, required=True)

class RegistroProveedorForm(forms.Form):
    razon_social=forms.CharField (max_length=50, required=True)
    contacto=forms.CharField (max_length=50, required=True)
    correo=forms.CharField(widget=forms.EmailInput)

# class LoginForm(forms.Form):
#     nombre=forms.CharField(widget=forms.TextInput)
#     password=forms.CharField(widget=forms.PasswordInput)

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {k:"" for k in fields}