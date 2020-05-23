from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username =forms.CharField(max_length=30, required=True, help_text='enter name.')
    phonenumber = forms.CharField(required=True,max_length=10)
    amount= forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ('username',  'email','phonenumber','amount', 'password1', 'password2', )