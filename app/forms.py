from django.forms import ModelForm
from .models import myapp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput )
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput )
    username = forms.CharField(max_length=100)

 


    class Meta:
        password1 = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
	
 
 

 
 
 
 
 
 
 
 
 
 
 

class TodoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = myapp