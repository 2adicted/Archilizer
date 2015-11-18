from django.shortcuts import render
from django.template import RequestContext

from .models import TrainingModule

# Create your views here.

def training(request):
	"""Trainings page"""
	trainings = TrainingModule.objects.all()

	return render(
		request,
		'trainings/trainings.html',
		context_instance = RequestContext(request,
			{			
			'trainings': trainings
			})
		)

def module(request, pk):
	"""Individual module references"""
	module = TrainingModule.objects.get(pk=int(pk))
	next = module.get_next()
	prev = module.get_prev()
	return render(
		request,
		'trainings/module.html',
		context_instance = RequestContext(request,
			{			
			'module': module,
			'next' : next,
			'prev' : prev,
			})
		)