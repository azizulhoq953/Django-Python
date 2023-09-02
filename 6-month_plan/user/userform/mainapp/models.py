from django.db import models

# Create your models here.
class authenticate(models.Model):
    username =models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)