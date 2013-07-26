from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    address = forms.CharField()
    website = forms.URLField()
