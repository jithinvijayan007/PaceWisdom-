from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    Fullname=models.CharField(max_length=100)
    role=(('Male','Male'),('Female','Female'))
    Gender=models.CharField(max_length=10,choices=role,default="Male")
    Mob_Number=models.CharField(max_length=12)
    Image=models.ImageField(default="default.jpg",upload_to="images",blank="True")
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Fullname
