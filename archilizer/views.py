from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect
from django.conf import settings
import stripe
from signup.forms import SignUpForm
from blog.models import Post

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

def donate(request):
    stripe_key = settings.STRIPE_KEYS['publishable']
    context = {'stripe_key': stripe_key,}
    return render(request, 'donate.html', context)

@csrf_exempt
def stripe_donation(request):
    if request.method == 'POST':
        amount = 1000
        stripe.api_key = settings.STRIPE_KEYS['secret']
        customer = stripe.Customer.create(
            email=request.POST.get('stripeEmail', ''),
            card=request.POST.get('stripeToken', '')
        )
        try:
            stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='eur',
                description='Archilizer donation'
            )
        except:
            return redirect('/')
        return redirect('/')
    return redirect('/')

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


class BlogSitemap(Sitemap):
	changefreq = "weekly"
	priority = 1.0

	def items(self):
		return Post.objects.filter(visible=True)

	def lastmod(self, obj):
		return obj.created

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', ]

    def location(self, item):
        return reverse(item)