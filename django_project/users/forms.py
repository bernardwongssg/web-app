from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # can set required to True or False
    
    class Meta: 
        model = User # when form.save() is called, it will be saved to 'User' model
        fields = ['username', 'email', 'password1', 'password2'] # password1 is password input, password2 is password validation

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # can set required to True or False
    
    class Meta: 
        model = User # when form.save() is called, it will be saved to 'User' model
        fields = ['username', 'email'] # password1 is password input, password2 is password validation

class ProfileUpdateForm(forms.ModelForm):
    class Meta: 
        model = Profile 
        fields = ['image']