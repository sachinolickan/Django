from django import forms

from userlogin.models import employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        exclude=('user_data',)

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']