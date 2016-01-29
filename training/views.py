from django.shortcuts import render
from django.template import RequestContext

from .models import TrainingModule

from signup.forms import SignUpForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def services(request):
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

	# gotodiv = False

	# if request_name(request) == 'development':
	# 	gotodiv = 'development'

	# elif request_name(request) == 'management':
	# 	gotodiv = 'management'

	# elif request_name(request) == 'training':
	# 	gotodiv = 'training'

	# TEST 
	# import pdb; pdb.set_trace()
	# TEST

	return render(
		request,
		'trainings/services.html',
		context_instance = RequestContext(request,
			{			
			'trainings': trainings,
			"form_signup" : form,
			# "gotodiv" : gotodiv,
			})
		)

# def request_name(request):
#     return request.path.split('/')[-2]
     

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