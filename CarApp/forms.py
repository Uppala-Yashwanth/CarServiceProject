from django import forms
from CarApp.models import Customer
from django.core.validators import RegexValidator
class DateInput(forms.DateInput):
    input_type = 'date'

class PasswordInput(forms.PasswordInput):
    input_type = 'password'

class CustomerForm(forms.ModelForm):
    Pickup_Date = forms.DateField(widget=DateInput())

    class Meta:
        model = Customer
        fields= ['cust_name','car_model','cust_phone','car_number','cust_addr','Pickup_Date','Email']


from django.contrib.auth.models import User
class signupform(forms.ModelForm):
    username = forms.CharField(max_length=120)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password', 'email']

