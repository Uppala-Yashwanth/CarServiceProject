# Generated by Django 4.1.1 on 2023-02-02 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_rename_customer_mechanic_cust_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mechanic',
            old_name='cust_name',
            new_name='car_number',
        ),
    ]