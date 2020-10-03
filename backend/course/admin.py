from django.contrib import admin

# Register your models here.
from .models import Company, Professor, Problem

admin.site.register(Company)
admin.site.register(Professor)
admin.site.register(Problem)
