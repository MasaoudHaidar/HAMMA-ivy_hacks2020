from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

from .models import *

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            fullname = form.cleaned_data.get('full_name')
            # get role from form and create corresponding account
            role = form.cleaned_data.get('role')
            if role == UserRegisterForm.STUDENT:
                student_user = Student(
                    user=User.objects.get(username=username),
                    full_name=fullname,
                )
                student_user.save()
            elif role == UserRegisterForm.COMPANY:
                company_user = Company(
                    user=User.objects.get(username=username),
                    full_name=fullname,
                )
                company_user.save()
            elif role == UserRegisterForm.PROFESSOR:
                professor_user = Professor(
                    user=User.objects.get(username=username),
                    full_name=fullname,
                )
                professor_user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

def login():
    return render(request, 'users/login.html')
