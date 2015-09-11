import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
# from tidbit.functions import uid_generator

class Entry(models.Model):
	uid = models.CharField(max_length=10)
	user = models.ForeignKey(User)
	text = models.CharField(max_length=300)
	date_created = models.DateField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=100, blank=True, null=True)
	public = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s entry: %s' % (self.user.username, self.date_created)

	def save(self, *args, **kwargs):
		if not self.id:
			self_uid = uid_generator()
		super(Entry, self).save(*args, **kwargs)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	slug = models.SlugField(blank=True, null=True)
	image = models.CharField(max_length=200, blank=True, null=True)
	# following = models.

	def __unicode__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user.get_full_name())
		super(UserProfile, self).save(*args, **kwargs)

