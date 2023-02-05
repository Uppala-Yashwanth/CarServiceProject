from django.db import models
from django.core.validators import RegexValidator
import re

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=105)
    car_model = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cust_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    car_number = models.CharField(max_length=25)
    cust_addr = models.CharField(max_length=100)
    Pickup_Date = models.DateField()
    Email= models.EmailField()
    def __str__(self):
        return self.cust_name




class Mechanic(models.Model):
    cust_name = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    Mech_name = models.CharField(max_length=100)
    Experience  = models.IntegerField()
    Delivery_Date  = models.DateField()
    def __str__(self):
        return self.Mech_name
