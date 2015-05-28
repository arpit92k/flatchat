from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

"""
UserProfle to store authorized users and custom data attributes
"""
class UserProfile(AbstractBaseUser):
	username=models.CharField(max_length=100)
	email = models.EmailField(max_length=100,blank=True)
	first_name = models.CharField(max_length=100,blank=True)
	last_name = models.CharField(max_length=100,blank=True)
	locality = models.CharField(max_length=500,blank=True)
	budget = models.IntegerField(blank=True)
	USERNAME_FIELD = 'username'
