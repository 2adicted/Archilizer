from django import forms

from crispy_forms.bootstrap import InlineField, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import SignUp

class SignUpForm(forms.ModelForm):

	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name


class ContactForm(forms.Form):
	full_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	message = forms.CharField(max_length=500, required=True)

	def clean_email(self):
		email = self.cleaned_data.get('email')		
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")

		return email
