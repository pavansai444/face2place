from django.db import models
from django.contrib.auth.models import User ,auth
from datetime import datetime
from django.utils import timezone
class journey(models.Model):
    journey_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    entry_location=models.CharField(max_length=200,default="")
    entry_time=models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    exit_location=models.CharField(max_length=200,default="")
    exit_time=models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    fare=models.IntegerField(default=10)

# class passengers(models.Model):
#     user_name = models.CharField(max_length=20)
#     photo = models.ImageField(upload_to='images/')
#     sex=models.CharField(max_length=20,default="Male")
#     status=models.CharField(max_length=20,default="NOT Travelling")
#     balance=models.IntegerField(default=1, blank=True, null=True)
#     password=models.CharField(max_length=20,default="**")
#     user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
#     age=models.IntegerField(default=1, blank=True, null=True)
#     phone=models.CharField(max_length=20,default="")
#     aadhar=models.CharField(max_length=20,default="")
#     place=models.CharField(max_length=20,default="")
#     last_visited_station=models.CharField(max_length=20,default="")

class passenger(models.Model):
    user_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    sex=models.CharField(max_length=20,default="Male")
    status=models.CharField(max_length=20,default="NOT Travelling")
    balance=models.IntegerField(default=1, blank=True, null=True)
    password=models.CharField(max_length=20,default="**")
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    age=models.IntegerField(default=1, blank=True, null=True)
    phone=models.CharField(max_length=20,default="")
    aadhar=models.CharField(max_length=20,default="")
    place=models.CharField(max_length=20,default="")
    last_visited_station=models.CharField(max_length=20,default="")
