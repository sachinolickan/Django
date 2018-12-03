from django import forms
from newapp.models import student,details,login



class registForm(forms.ModelForm):
    class Meta:
        model=student
        exclude=('created_date',)

class imgForm(forms.ModelForm):
    class Meta:
        model=details
        exclude=('created_date',)

class loginForm(forms.ModelForm):
    class Meta:
        model=login
        exclude = ('created_date',)