from django.shortcuts import render
from django.template import RequestContext

from newsletter.forms import SignUpFormConstruction
# Create your views here.
def about(request):
	"""About us page"""
	return render(
		request,
		'about_us.html',
		context_instance = RequestContext(request,
			{
			})
		)

def under_construction(request):
	"""Under Construction home view"""
	title = "Under Construction"

	#add form
	form = SignUpFormConstruction(request.POST or None)

	if form.is_valid():
		instance = form.save()

	return render(
		request,
		'uc/uc_home.html',
		context_instance = RequestContext(request,
			{
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



