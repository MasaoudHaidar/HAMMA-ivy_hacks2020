from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Company)
# admin.site.register(Professor)
# admin.site.register(Student)
admin.site.register(Problem)
admin.site.register(Discussion)
admin.site.register(Solution)
