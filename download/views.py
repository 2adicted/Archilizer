
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def download(request):
	""" Main downloads section """
	title = 'downloads'

	return render(
		request,
		'downloads/base.html',
		context_instance = RequestContext(request,
			{
			"title": title,
			})
		)