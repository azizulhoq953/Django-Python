from django.db import models
import django.contrib.auth

# Create your models here.
class login(models.Model):
  
    uname = models.CharField(max_length=50)
    psw = models.EmailField(max_length=50)
    remember = models.TextField(max_length=35)
    # phone = models.CharField(max_length=50)
    # subject = models.TextField(max_length=55)
    # message = models.TextField(max_length=100)

def _str_(self):
        return self.Password


