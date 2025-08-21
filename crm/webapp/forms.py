from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import Client

from django.forms.widgets import PasswordInput, TextInput


# Register / Create a user
class CreateUserForm(UserCreationForm):

    class Meta:
    
        model = User
        fields = ['username', 'password1', 'password2']


# Login a User
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


# Create a client
class AddClientForm(forms.ModelForm):

    class Meta:
    
        model = Client
        fields = ['first_name' , 'last_name', 'email', 'phone_number', 'address', 'city', 'province', 'country']


# Update client record
class UpdateClientForm(forms.ModelForm):

    class Meta:
    
        model = Client
        fields = ['first_name' , 'last_name', 'email', 'phone_number', 'address', 'city', 'province', 'country']
