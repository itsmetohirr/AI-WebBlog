# ai_blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Email'
        })
        )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Username'
            }),
        }
