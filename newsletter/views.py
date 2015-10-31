from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import RequestContext

from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = "Welcome"

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = forms.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()

	# if form.is_valid():

	return render(
		request,
		'home.html',
		context_instance = RequestContext(request,
			{
			"title": "Thank you Sir/Madam",
			"form" : form,
			})
		)

def contact(request):
	title = 'Contact Us'
	text_align_true = True
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

	return render(
		request,
		'forms.html',
		context_instance = RequestContext(request,
			{			
			"form" : form,
			"title" : title,
			 "text_align_true" : text_align_true,
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





