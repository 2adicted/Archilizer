from django.contrib import admin

from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	search_field = ['title', 'created']
	list_display = ['__unicode__', 'created']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post", "author", "craeted"]

admin.site.register(Comment,CommentAdmin)
