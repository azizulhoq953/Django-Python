from django.db import models

# Create your models here.

class myapp(models.Model):
    text = models.CharField(max_length=200)
