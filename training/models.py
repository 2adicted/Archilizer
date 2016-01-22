from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile

from cStringIO import StringIO
from PIL import Image

import image, os


# Create your models here.
class TrainingModule(models.Model):
	title = models.CharField(max_length=30, unique=True)
	short_description = models.CharField(max_length=30)
	slug = models.SlugField(max_length=40, unique=True)
	description = models.TextField()
	objective = models.TextField()
	structure = models.TextField()
	duration = models.CharField(max_length=30, blank=True, null=True)
	price = models.CharField(max_length=30)
	location = models.CharField(max_length=30, blank=True)
	level = models.CharField(max_length=30)
	attendants = models.DecimalField(max_digits=2, decimal_places=0)
	image = models.ImageField(upload_to='modules/')
	url = 'module'
	
	def __unicode__(self):
		return self.title

	def get_next(self):
		next = TrainingModule.objects.filter(id__gt=self.id)
		if next:
			return next[0].id
		return self.id

	def get_prev(self):
		prev = TrainingModule.objects.filter(id__lt=self.id).order_by('-id')
		if prev:
			return prev[0].id
		return self.id
