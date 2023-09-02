from django.db import models

# Create your models here.
class main(models.Model):
 main_ID = models.IntegerField(),
 main_Name = models.CharField(),
 main_Email = models.EmailField(),