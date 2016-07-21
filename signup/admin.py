from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .forms import SignUpForm
from .models import SignUp, Newsletter, Message, Subscription, Submission

# Register your models here.
class CreateSignUp(admin.ModelAdmin):
	list_display = ['__unicode__', 'full_name', 'updated', ]
	form = SignUpForm

admin.site.register(SignUp, CreateSignUp)

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = '__all__'


	users = forms.ModelMultipleChoiceField(
		queryset=SignUp.objects.all(), 
		required=False,
		widget=FilteredSelectMultiple(
			verbose_name='SignUp', 
			is_stacked=False
			)
		)

	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['users'].initial = self.instance.user.all()

	def save(self, commit=True):
		subscription = super(SubscriptionForm, self).save(commit=False)
		if commit:
			subscription.save()

		if subscription.pk:
			subscription.user = self.cleaned_data['users']
			self.save_m2m()

		return subscription


class SubscriptionAdmin(admin.TabularInline):
	model = Subscription
	extra = 1


class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'title', 'email', 'sender',  ]
	prepopulated_fields = {"slug": ("title", )}
	# inlines = [SubscriptionAdmin]
	# form = SubscriptionForm
	search_field = ['title', ]

admin.site.register(Newsletter, NewsletterAdmin)

class MessageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'newsletter', ]
	prepopulated_fields = {"slug": ("title", )}
	search_field = ['title', ]

admin.site.register(Message, MessageAdmin)

class SubmissionAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'message', 'published', ]

admin.site.register(Submission, SubmissionAdmin)