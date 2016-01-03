from django.shortcuts import render
from django.template import RequestContext

from .models import TrainingModule

from newsletter.forms import SignUpForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def training(request):
	"""Trainings page"""
	trainings = TrainingModule.objects.all()

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
		'trainings/trainings.html',
		context_instance = RequestContext(request,
			{			
			'trainings': trainings,
			"form_signup" : form,
			})
		)

@csrf_exempt
def module(request, pk):
	"""Individual module references"""
	module = TrainingModule.objects.get(pk=int(pk))
	next = module.get_next()
	prev = module.get_prev()

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
		'trainings/module.html',
		context_instance = RequestContext(request,
			{			
			'module': module,
			'next' : next,
			'prev' : prev,
			"form_signup" : form,
			})
		)