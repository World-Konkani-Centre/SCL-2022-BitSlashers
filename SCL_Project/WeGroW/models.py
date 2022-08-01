from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    role=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    
    