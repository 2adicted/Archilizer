from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from signup.forms import SignUpForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def about(request):
	"""About us page"""

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('thankyou')
		
	return render(
		request,
		'about_us.html',
		context_instance = RequestContext(request,
			{
			"form_signup" : form,
			})
		)

@csrf_exempt
def under_construction(request):
	"""Under Construction home view"""
	title = "Under Construction"

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('thankyou')

	return render(
		request,
		'uc/uc_home.html',
		context_instance = RequestContext(request,
			{
			"title": title,
			"form" : form,
			})
		)

def under_construction_subscribed(request):
	"""Under Construction subscribed view"""
	title = "Under Construction - thank you for subscribing."

	return render(
		request,
		'uc/uc_sub.html',
		context_instance = RequestContext(request,
			{
			})
		)



