from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

    
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=254)
    profile_pic = models.ImageField(upload_to='profile_pics/',default='profile_pics/avatar.png')

class Neighborhood(models.Model):
    location = models.CharField(max_length=100, default='Kibra')
    # occupants = models

    def __str__(self):
        return self.location

class Hood(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hoods')
    name = models.CharField(max_length=240)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    @classmethod
    def get_user_hood(cls, user):
        hood = cls.objects.get(user=user)
        return hood


    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=240)
    description = models.TextField()
    category = models.CharField(max_length=240)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE,related_name='businesses')
    contacts = models.CharField(max_length=240,default='addcontacts')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='businesses')

    def __str__(self):
        return self.name

class PublicService(models.Model):
    SERVICE_CHOICES = (
        ('police', 'Police Department'),
        ('health', 'Health & Sanitary Department'),
    )
    name = models.CharField(max_length=240)
    category = models.CharField(max_length=100,choices=SERVICE_CHOICES)
    contacts = models.CharField(max_length=240)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE,related_name='public_services')

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=240)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    hood = models.ForeignKey(Hood,on_delete = models.CASCADE,related_name='posts')
    posted = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title