from django.db import models

# Create your models here.
class Messages(models.Model):
	fb_id = models.CharField(max_length = 128, unique = True)
	name = models.CharField(max_length = 50)
	profile_url = models.URLField()
	locale = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 10)
	message = models.CharField(max_length = 1000)

	def __unicode__(self):
		return self.name

class Users(models.Model):
	fb_id = models.CharField(max_length = 128, unique = True)
	email = models.CharField(max_length = 50)
	batch = models.URLField()
	
	def __unicode__(self):
		return self.email