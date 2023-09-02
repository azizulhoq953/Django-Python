from django.db import models
import django.contrib.auth


# Create your models here.

class login(models.Model):
  
    username = models.CharField(max_length=55)
    email = models.EmailField(max_length=33)
    phone = models.CharField(max_length=15)
    subject = models.TextField(max_length=55)
    message = models.TextField(max_length=100)

def _str_(self):
        return self.Password



class blogAdmin(models.Model):
      title = models.CharField( max_length=50, help_text="title")
      description = models.TextField()
      image = models.ImageField()
      date =models.DateTimeField(auto_now_add= True)
    
def _str_(self):
        return self.description
      


 
   


# class singup(models.Model):
#     Usearname = models.CharField(max_length=20)
#     Password = models.IntegerField(max_length=30)

#     def _str_(self):
#         return self.Password
#     create_newObj = models.Manager()
  

