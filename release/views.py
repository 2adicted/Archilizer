from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from signup.forms import SignUpForm

# Create your views here.
def main(request):
	title = "Recent Revit Plugin Releases by Archilizer"
	""" Main listing """
	

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
		'release/main.html',
		context_instance = RequestContext(request,
			{
			"title" : title,
			"form_signup" : form,
			})
		)