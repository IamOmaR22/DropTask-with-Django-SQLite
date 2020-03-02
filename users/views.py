from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration Is Completed, Login To Get Started')
            return redirect('login')
    else:
        register_form = CustomRegisterForm()

    return render(request, 'register.html', {'register_form':register_form})