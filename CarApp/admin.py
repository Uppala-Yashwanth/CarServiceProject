from django.contrib import admin
from CarApp.models import Customer,Mechanic
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cust_name','cust_phone','car_number','cust_addr','car_model','Pickup_Date','Email']

admin.site.register(Customer,CustomerAdmin)


class MechAdmin(admin.ModelAdmin):
    list_display = ['cust_name', 'Mech_name','Experience','Delivery_Date']

admin.site.register(Mechanic,MechAdmin)



