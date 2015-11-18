from django.contrib import admin

from .models import TrainingModule

# Register your models here.


class TrainingModuleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ['__unicode__', 'short_description',]

admin.site.register(TrainingModule, TrainingModuleAdmin)

