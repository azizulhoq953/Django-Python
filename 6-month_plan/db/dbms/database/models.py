from django.db import models

# Create your models here.
class Student_info(models.Model):
    std_ID = models.IntegerField(max_length=30),
    std_Name = models.CharField(),
    std_Email = models.EmailField(),