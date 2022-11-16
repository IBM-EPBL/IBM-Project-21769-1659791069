from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import AboutForm, quote
from django.forms import ModelForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Aboutforms(ModelForm):
    class Meta:
        model = AboutForm
        fields = '__all__'

class Quoteform(ModelForm):
    class Meta:
        model = quote
        fields = '__all__'
