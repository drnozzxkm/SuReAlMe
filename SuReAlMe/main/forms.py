from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com'}))
    rol = forms.ChoiceField(label='Rol', choices=User.ROLE_CHOICES)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Crea una contraseña'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Repite la contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'rol', 'password1', 'password2']
