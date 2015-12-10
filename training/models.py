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
	thumb_image = models.ImageField(upload_to='modules/')

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

	def save(self, *args, **kwargs):
		"""On save,update image size"""

		if self.thumb_image:
			self.create_thumbnail()
			pass
		
		return super(TrainingModule, self).save(*args, **kwargs)

	def create_thumbnail(self):
         # original code for this method came from
         # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

         # If there is no image associated with this.
         # do not create thumbnail
         if not self.thumb_image:
             return

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (500,500)

         DJANGO_TYPE = self.thumb_image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         thumb_image = Image.open(StringIO(self.thumb_image.read()))

         # Convert to RGB if necessary
         # Thanks to Limodou on DjangoSnippets.org
         # http://www.djangosnippets.org/snippets/20/
         #
         # I commented this part since it messes up my png files
         #
         #if image.mode not in ('L', 'RGB'):
         #    image = image.convert('RGB')

         # We use our PIL Image object to create the thumbnail, which already
         # has a thumbnail() convenience method that contrains proportions.
         # Additionally, we use Image.ANTIALIAS to make the image look better.
         # Without antialiasing the image pattern artifacts may result.
         thumb_image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         thumb_image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.thumb_image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.thumb_image.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

