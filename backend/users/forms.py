from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    name = forms.EmailField()
    email = forms.EmailField()
    role = forms.ChoiceField(choices = ((1, "Student"),
    (2, "Company"),
    (3, "Professor")))

    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'password1', 'password2']