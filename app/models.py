from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    profile_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.fullname