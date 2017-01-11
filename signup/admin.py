from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# Register your models here.
class CreateSignUp(admin.ModelAdmin):
	list_display = ['__unicode__', 'full_name', 'updated', ]
	form = SignUpForm

admin.site.register(SignUp, CreateSignUp)