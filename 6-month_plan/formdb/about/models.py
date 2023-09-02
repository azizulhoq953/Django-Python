from django.db import models

# Create your models here.

class teacher(models.Model):
    Tid = models.IntegerField()
    TName = models.CharField(max_length=50)
    TEmail = models.EmailField()
    TAddress = models.CharField(max_length=100, null=True) # True type then auto success
    