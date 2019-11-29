from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=254)

class Neighborhood(models.Model):
    location = models.CharField(max_length=100, default='Kibra')
    # occupants = models

    def __str__(self):
        return self.location

class Hood(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hoods')
    name = models.CharField(max_length=240)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


