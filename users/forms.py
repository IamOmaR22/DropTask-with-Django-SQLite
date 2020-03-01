from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField() ## By default required=True, if i want to skip this field while register then required=False


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
