from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='userprofile_user')
	bio = models.TextField(max_length=250, blank=True)

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
	"""Create a profile for the registered user."""

	user = kwargs['instance']

	if kwargs['created']:
		user_profile = UserProfile(user=user)
		user_profile.save()