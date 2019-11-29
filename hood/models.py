from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=254)

class Neighborhood(models.Model):
    name = models.CharField(max_length=100, default='Kibra')

    def __str__(self):
        return self.name    

