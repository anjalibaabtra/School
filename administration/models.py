from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AdminUser(AbstractUser):
    # Name = models.TextField(max_length=100,default='')
    # Firstname = models.TextField(max_length=100,default='')
    # Lastname = models.TextField(max_length=100,default='')
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Students(models.Model):
    Name = models.TextField(max_length=100,default='')
    Contact = models.BigIntegerField(default=0)
    Email = models.EmailField(max_length=100,default='')
    Username = models.TextField(max_length=100,default='')
    Password = models.TextField(max_length=100,default='')
    active = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=True)