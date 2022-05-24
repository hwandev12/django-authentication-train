from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import CustomUserModel


class CustomUserModelCreate(UserCreationForm):
    parent_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Parent Name',
            'class': 'form-control',
        }))
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
        }))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
        }))
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control',
                             }))
    phone = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'placeholder': '+998',
            'class': 'form-control',
        }), required=True)
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))

    class Meta:
        model = CustomUserModel
        fields = ('first_name', 'last_name', 'parent_name', 'phone', 'username', 'email')
