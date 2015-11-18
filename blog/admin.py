from django.contrib import admin
# from django.contrib.auth.models import User

from .models import Post, Comment, Category, CategoryToPost

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	
admin.site.register(Category,CategoryAdmin)

class CategoryToPostInline(admin.TabularInline):
	model = CategoryToPost
	extra = 1

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	search_field = ['title', 'created']
	list_display = ['__unicode__', 'created',]
	inlines = [CategoryToPostInline]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post", "author", "craeted"]

admin.site.register(Comment,CommentAdmin)