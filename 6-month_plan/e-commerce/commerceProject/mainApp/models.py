from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.


# class cartdb (models.Model):

#   Item = models.CharField(max_length=100),
#   Price = models.IntegerField(max_length=10000),
#   Quantity = models.IntegerField(max_length=5),
#   Total = models.IntegerField(max_length=100),
 
# def _str_(self):
#         return self.Price

# class Deleted(models.Model):
#     question = models.ForeignKey(cartdb, on_delete=models.CASCADE),
#     Deleted_text = models.CharField(),
#     votes = models.IntegerField(default=0, max_length=100),

# def _str_(self):
#         return self.Deleted_text


class shopAdmin(models.Model):
      Name = models.CharField( max_length=50, help_text="ChairName")
      price = models.FloatField(max_length=6, help_text="Price")
      image = models.ImageField()
      date =models.DateTimeField(auto_now='date')
    
def _str_(self):
        return self.price



class authenticate (models.Model):
      Username = models.CharField(max_length=50)
      Email = models.EmailField(null=True) 
      PhoneNumber = models.CharField(max_length=12)
      Password = models.CharField( max_length=50,null=True)
      Password1 = models.CharField( max_length=50,null=True)
      Location = models.TextField()

def _str_(self):
        return self.Username


class login(models.Model):
      email = models.EmailField()
      password = models.IntegerField()


def _str_(self):
        return self.password


class defaultd(models.Model):
      username = models.OneToOneField(User, on_delete=models.CASCADE)
      password1 = forms.CharField(widget=forms.PasswordInput)
