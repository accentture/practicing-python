
#creating a form based in a model of django

from django import forms
from django.core import validators

#importin form of django
from django.contrib.auth.forms import UserCreationForm

#importing model of user provided by django
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] #two password to confirm password inserted by user


