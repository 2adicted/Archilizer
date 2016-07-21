import datetime

from django.db import models

from tinymce.models import HTMLField

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
DEFAULT_MESSAGE_ID = 1

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(unique=True)
	full_name = models.CharField(max_length=120, blank=True, null=True, unique=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email

class Newsletter(models.Model):
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=40, unique=True)
	email = models.EmailField(unique=True)
	sender = models.CharField(max_length=60)
	user = models.ManyToManyField(SignUp, through='Subscription')

	def __unicode__(self):
		return self.title

class Message(models.Model):	
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=40, unique=True)
	body = HTMLField()
	newsletter = models.ForeignKey(Newsletter)

	def __unicode__(self):
		return self.title

# class NewsletterToSubscribe(models.Model):

		
class Subscription(models.Model):
	class Meta:
		auto_created = True
		
	newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
	user = models.ForeignKey(SignUp, on_delete=models.CASCADE)
	status = models.BooleanField(choices=BOOL_CHOICES,default=1)
	subscribe = models.DateTimeField(auto_now_add=False, auto_now=True)
	unsubscribe = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.newsletter.title


class Submission(models.Model):
	message = models.ForeignKey(Message, default=DEFAULT_MESSAGE_ID)
	published = models.DateTimeField(editable=True)

	def __unicode__(self):
		return self.message.title


