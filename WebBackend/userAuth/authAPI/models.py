from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	about = models.CharField(max_length=500, blank=True, default='')
	owner = models.ForeignKey('auth.User', related_name='about')
