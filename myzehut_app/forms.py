from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username','password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'login-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'login-password',
        'placeholder': 'password',
        'required': True
      }),
    } 