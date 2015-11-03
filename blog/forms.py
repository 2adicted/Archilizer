from django.forms import ModelForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		""" created, author, body, post """
		model = Comment
		exclude = ["post"]
