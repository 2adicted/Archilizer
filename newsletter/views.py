from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from .forms import SignUpForm, ContactForm
from blog.models import Post
from training.models import TrainingModule

# Create your views here.
def home(request):
	title = "Revit Training | BIM Consultancy | Revit Plugins & Custom Tools "

	#add blog-posts	
	posts = Post.objects.all().order_by("-created")[:3]

	#add services (have to rename them)
	services = TrainingModule.objects.all()[:3]

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')

	return render(
		request,
		'home.html',
		context_instance = RequestContext(request,
			{
			"title": title,
			"form" : form,
			"posts" : posts,
			"services" : services,
			})
		)

def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)

	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get('full_name')
		# print email, message, full_name
		subject = 'Archilizer contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = from_email
		contact_message = '''
		%s: %s via %s
		'''%(form_full_name, form_message, form_email)

		send_mail(subject, 
			contact_message, 
			from_email, 
			[to_email], 
			fail_silently=False)

		return HttpResponseRedirect(reverse('thanks'))

	return render(
		request,
		'forms.html',
		context_instance = RequestContext(request,
			{			
			"form" : form,
			"title" : title,
			})
		)

def thanks(request):
	title = 'Thank you'

	return render(
		request,
		'thanks.html',
		context_instance = RequestContext(request,
			{			
			"title" : title,
			})
		)


def example(request):

	return render(
		request,
		'example.html',
		context_instance = RequestContext(request,
			{
			})
		)





