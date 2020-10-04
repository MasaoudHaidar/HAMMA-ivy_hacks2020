from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

# Register your models here.
class StudentsInline(admin.StackedInline):
    model = Student
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inline = (StudentsInline, )

admin.site.register(User, UserAdmin)
admin.site.register(Company)
admin.site.register(Professor)
admin.site.register(Student)
