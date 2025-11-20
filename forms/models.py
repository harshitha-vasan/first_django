from django.db import models

# Create your models here.
class formDetails(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField(null=True)
    comment=models.CharField(max_length=255)