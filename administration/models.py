from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AdminUser(AbstractUser):
    Name = models.TextField(max_length=100,default='')
    Firstname = models.TextField(max_length=100,default='')
    Lastname = models.TextField(max_length=100,default='')
