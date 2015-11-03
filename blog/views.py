import time
from calendar import month_name
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from .models import Post, Comment
from .forms  import CommentForm
# Create your views here.

def main(request):
	""" Main listing """
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 12)

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
	 		"months" : mkmonth_lst(),
			})
		)

def month(request, year, month):
	"""Monthly archive."""
	posts = Post.objects.filter(created__year=year, created__month=month)
	print (posts)
	return render(
	request,
	'blog/list.html',
	context_instance = RequestContext(request,
		{
		"posts" : posts,
	 	"user": request.user,
	 	"months" : mkmonth_lst(),
	 	"archive" : True,
		})
	)



def post(request, pk):
	"""Single post with comments and a comment form."""
	post = Post.objects.get(pk=int(pk))
	comments = Comment.objects.filter(post=post)

	return render(
	request,
	'blog/post.html',
	context_instance = RequestContext(request,
		{
		"post" : post,
		"comments": comments,
		"form": CommentForm(), 
	 	"user": request.user,
		})
	)


def add_comment(request, pk):
	""" Add a new comment. """
	p = request.POST
	print (str(pk))
	if p.has_key("body") and p["body"]:
		author = "Anonymous"
		if p["author"]: author = p["author"]

		comment = Comment(post=Post.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False

		comment = cf.save(commit=False)
		comment.author = author
		comment.save()
	return HttpResponseRedirect(reverse("blog-post", args=(pk,)))

def mkmonth_lst():
	"""Make a list of months to show archive links."""
	if not Post.objects.count(): return []
	# set up vars
	year, month = time.localtime()[:2]
	first = Post.objects.order_by("created")[0]
	fyear = first.created.year
	fmonth = first.created.month
	months = []

	# loop over years and months
	start, end = 12, 0
	for y in range(year, fyear-1, -1):
		if y == year: start = month
		if y == fyear: end = fmonth -1

		for m in range (start, end, -1):
			months.append((y, m, month_name[m]))
	
	return months
