from django.db import models
from django.contrib import admin
# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=100,help_text="Enter Customer Name")
    dob=models.DateField(help_text="Enter Date of Birth")
    customer_email=models.CharField(help_text="Enter Customer Email")
    customer_address=models.CharField(max_length=200,help_text="Enter Customer Address")
class CustomerAdmin(admin.ModelAdmin):
    list_display=('customer_name','dob','customer_email','customer_address')p