from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=50, required=True)

    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())
    # avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1',
            'password2'
        ]


class LogInForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')
