from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    role=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    
class Product(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=300)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()
    phone_number=models.CharField(max_length=10)
    seller_country=models.CharField(max_length=20)
    seller_state=models.CharField(max_length=20)
    seller_district=models.CharField(max_length=20)
    pin_code=models.IntegerField()
    
class Contact_us(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=300)