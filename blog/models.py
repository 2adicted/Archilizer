from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from cStringIO import StringIO
from tinymce import models as tinymce_models
from PIL import Image

import image, os

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=40, unique=True)
	body = tinymce_models.HTMLField()
	created = models.DateTimeField(editable=True)
	categories = models.ManyToManyField('Category', blank=True, through='CategoryToPost')
	image = models.ImageField(upload_to='blogposts/');

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		"""On save, update timestamps and image size"""
		if not self.id:
			self.created = timezone.now()

		if self.image:
			self.create_thumbnail()
			pass
		
		return super(Post, self).save(*args, **kwargs)

	def create_thumbnail(self):
         # original code for this method came from
         # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

         # If there is no image associated with this.
         # do not create thumbnail
         if not self.image:
             return

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (500,500)

         DJANGO_TYPE = self.image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(StringIO(self.image.read()))

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
         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.image.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

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
			message = "Comment was added to '%s' by '%s': \n\n%s" % (self.post, self.author, self. body)

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

