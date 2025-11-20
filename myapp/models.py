from django.db import models

# Create your models here.
class contactDetails(models.Model):
    name=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    phone=models.BigIntegerField(null=True)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=255)
    screenshot=models.ImageField(null=True)
    session_id=models.EmailField(null=True)


class registerDetails(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=16)

class productDetails(models.Model):
    product_id=models.CharField(max_length=7)
    product_name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.FloatField() 