from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	""" custom user model """
	Position = models.CharField(max_length=100, null='', blank = True)

	def __str__(self):
		return self.username
	


