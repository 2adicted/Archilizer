from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
def about(request):

	return render(
		request,
		'about_us.html',
		context_instance = RequestContext(request,
			{
			})
		)