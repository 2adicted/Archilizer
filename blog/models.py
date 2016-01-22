from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from cStringIO import StringIO
from tinymce.models import HTMLField
from PIL import Image

import image, os

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=40, unique=True)
	body = HTMLField()
	created = models.DateTimeField(editable=True)
	categories = models.ManyToManyField('Category', blank=True, through='CategoryToPost')
	image = models.ImageField(upload_to='blogposts/');
	visible = models.BooleanField(default=True);
	url = 'blog-post'
	
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		"""On save, update timestamps"""
		if not self.id:
			self.created = timezone.now()

		return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))
	
	def save(self, *args, **kwargs):
		"""Email when a comment is added."""
		if "notify" in kwargs and kwargs["notify"] == True:
			message = "Comment was added to '%s' by '%s': \n\n%s" % (self.post, self.author, self.body)

			subject = 'Archilizer contact form'
			from_email = settings.EMAIL_HOST_USER
			to_email = from_email

			send_mail("New comment added", message, from_email, [to_email])

		if "notify" in kwargs: del kwargs["notify"]

		super(Comment, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, unique=True)
	description = models.TextField()
	posts = models.ManyToManyField('Post', blank=True, through='CategoryToPost')

	class Meta:
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/categories/%s/" % self.slug

class CategoryToPost(models.Model):
	post = models.ForeignKey(Post)
	caregory = models.ForeignKey(Category)

