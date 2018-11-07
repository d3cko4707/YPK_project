from django.forms import ModelForm
from django import forms
from .models import *

class SignUpForm(ModelForm):
    first_name = forms.CharField(label='First_name')
    last_name = forms.CharField(label='last_name', required=True)
    email = forms.EmailField(label='email', required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']



class MembershipForm(ModelForm):
    class Meta:
        model = Register
        fields = ['gender', 'first_name', 'last_name', 'county', 'address',
                  'postcode', 'city', 'phone', 'mobilephone', 'fax', 'workphone']

