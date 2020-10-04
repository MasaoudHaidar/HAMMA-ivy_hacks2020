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
            # get role from form and create corresponding account
            role = form.cleaned_data.get('role')
            if role == UserRegisterForm.STUDENT:
                student_user = StudentUser(
                    user=User.objects.get(username=username),
                )
                student_user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('course:index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

def login():
    pass
