from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from .models import *
# Create your views here.

def main(request):
	""" Main listing """
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)

	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render(
		request,
		'blog/list.html',
		context_instance = RequestContext(request,
			{
			"title": 'Blog',
			"posts": posts, 
		 	"user" : request.user,
			})
		)

def post(request, pk):
	""" Single post with comments and a comment form. """
	post = Post.objects.get(pk=int(pk))

	return render(
		request,
		'blog/post.html',
		context_instance = RequestContext(request,
			{
			"title": 'Blog',
			"post": post, 
		 	"user": request.user,
			})
		)

def add_comment(request, pk):
	""" Add a new comment. """
	p = request.POST

	if p.has_key("body") and p["body"]:
		author = "Anonymous"
		if p["author"]: aythor = p["author"]

		comment = Comment(post=Post.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False

		comment = cf.save(commit=False)
		comment.author = author
		comment.save()
	return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))

	def post(request, pk):
		"""Single post with comments and a comment form."""
		post = Post.objects.get(pk=int(pk))
		comments = Comment.objects.filter(post=post)

		return render(
		request,
		'blog/post.html',
		context_instance = RequestContext(request,
			{
			"comments": comments,
			"form": ComentForm(), 
		 	"user": request.user,
			})
		)

