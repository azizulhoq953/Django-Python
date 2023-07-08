from django.db import models

# Create your models here.

class djangoenv(models.Model):
    text = models.CharField(max_length=200)
