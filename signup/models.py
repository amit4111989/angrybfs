from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	PANDA=0
	HYENA=1
	JELLYFISH=2
	COBRA=3

	GROUP_CHOICES = (
		(PANDA,'panda'),
		(HYENA, 'hyena'),
		(JELLYFISH,'jellyfish'),
		(COBRA, 'cobra')
		)
	user_group = models.IntegerField(max_length=1,choices=GROUP_CHOICES,default=PANDA)
	tagline = models.CharField(max_length=200)


	def __unicode__(self):
		return self.tagline
	