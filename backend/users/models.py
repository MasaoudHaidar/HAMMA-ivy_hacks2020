from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class StudentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # school = models.CharField(max_length=100)
    # is_student = models.BooleanField(default=False)
    # is_professor = models.BooleanField(default=False)
    # is_company = models.BooleanField(default=False)
