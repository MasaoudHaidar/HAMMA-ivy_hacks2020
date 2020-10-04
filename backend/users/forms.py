from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    STUDENT = 'ST'
    COMPANY = 'COM'
    PROFESSOR = 'PROF'
    role = forms.ChoiceField(choices=[
        (STUDENT, "Student"),
        (COMPANY, "Company"),
        (PROFESSOR, "Professor")
    ])

    class Meta:
        model = models.User
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'role']
