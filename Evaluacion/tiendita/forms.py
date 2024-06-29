# forms.py
from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'telefono', 'contrasena']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['contrasena'])
        if commit:
            user.save()
        return user
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'telefono']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email', max_length=100)
