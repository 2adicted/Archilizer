from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from itertools import chain

from .forms import SignUpForm, ContactForm
from blog.models import Post
from training.models import TrainingModule

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def home(request):
	title = "BIM Management | Revit Training | Revit Plugins & Custom Tools "

	#add blog-posts	
	posts = Post.objects.all().order_by("-created").filter(visible=True)

	#add services (have to rename them)
	services = TrainingModule.objects.all()[:3]

	#concatenate the two lists
	result_list = list(chain(posts, services))[:6]

	#no pagination for now

	# paginator = Paginator(result_list, 6)

	# page = request.GET.get('page')
	# try:
	# 	results = paginator.page(page)
	# except PageNotAnInteger:
	# 	results = paginator.page(1)
	# except EmptyPage:
	# 	contacts = paginator.page(paginator.num_pages)

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
			"form_signup" : form,
			"posts" : posts,
			"services" : services,
			"results" : result_list,
			})
		)


@csrf_exempt
def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	form_signup = SignUpForm(request.POST or None)

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

	if form_signup.is_valid():
		instance = form_signup.save(commit=False)
		full_name = form_signup.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')

	return render(
		request,
		'forms.html',
		context_instance = RequestContext(request,
			{			
			"form_signup" : form_signup,
			"form" : form,
			"title" : title,
			})
		)

def thanks(request):
	title = 'Thank you'
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
		'thanks.html',
		context_instance = RequestContext(request,
			{			
			"title" : title,
			"form_signup" : form,
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





