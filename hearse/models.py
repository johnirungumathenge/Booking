from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.

class Hearse(models.Model):
    driver_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    color = models.TextField(default='black')
    model = models.TextField(default=2016)
    driver_phone = models.IntegerField()
    Price = models.IntegerField(default=0)
    location = models.TextField(default="Nakuru")
    hearse_image = models.ImageField(upload_to='hearse_img/', null=True, blank=True)
    description = models.TextField(default="located in Nakuru")

    def __str__(self):
        return self.driver_name

    


class Request(models.Model):
    fullname = models.CharField(max_length=100, default='name')
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='@gmail.com')
    Day = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True)
    
    
