from django.db import models
from django.db.models import User

# Create your models here.

class signup(models.Model):
	user = models.ForeignKey(User)
	