from django.db import models

# Create your models here.

class portfolio(models.Model):
  
    username = models.CharField(max_length=55)
    email = models.EmailField(max_length=33)
    message = models.TextField(max_length=100)

def _str_(self):
        return self.Password
