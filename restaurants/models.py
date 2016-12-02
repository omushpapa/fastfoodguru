from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=150, blank=False)
	location = models.OneToOneField('Location', blank=False)

class Location(models.Model):
	street = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50, blank=False)
	state = models.CharField(max_length=50, blank=False)
	country = models.CharField(max_length=60, blank=False)

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile_user')
	bio = models.TextField(max_length=250, blank=True)

class Review(models.Model):
	restaurant = models.OneToOneField('Restaurant', related_name='review_restaurant')
	user = models.OneToOneField(User, related_name='review_user')
	bathroom = models.CharField(max_length=250, blank=True)
	staff = models.CharField(max_length=250, blank=True)
	cleanliness = models.CharField(max_length=250, blank=True)
	drive_through_sassy = models.CharField(max_length=250, blank=True)
	delivery_speed = models.CharField(max_length=250, blank=True)
	other = models.CharField(max_length=250, blank=True)
	
