from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    empid = models.IntegerField(unique=True,blank=True)
    mobile = models.CharField(max_length=13,blank=True)
    dept = models.CharField(max_length=50,blank=True)
    last_modified = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return str(self.user)

class vehicle_master(models.Model):
    vehicle_name = models.CharField(max_length=60)
    vehicle_type = models.CharField(max_length=50)
    last_modified = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return str(self.vehicle_name)

class booking(models.Model):
    CHOICES = (
        ('','Click to Select'),
        ('Ambulance','Ambulance'),
        ('Office Vehicle','Office Vehicle'),
        
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    vehicle_id = models.IntegerField(null=True,blank=True)
    vehicle_name = models.CharField(max_length=60,blank=True)
    vehicle_type = models.CharField(max_length=50,choices=CHOICES,default="CHOICES[0][0]")
    driver_details = models.CharField(max_length=120,blank=True)
    last_modified = models.DateTimeField(auto_now_add=True,blank=True)
    booking_status = models.BooleanField(blank=True,default=0)

    def  __str__(self):
        return str(self.destination)

    @property
    def today(self):
        return date.today()


class role_master(models.Model):
    empid = models.OneToOneField(User,on_delete=models.CASCADE)
    is_admin = models.BooleanField(blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return str(self.empid)




