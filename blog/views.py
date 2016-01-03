import time
from calendar import month_name
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from .models import Post, Comment, Category
from .forms  import CommentForm

from newsletter.forms import SignUpForm
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

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')

	return render(
		request,
		'blog/list.html',
		context_instance = RequestContext(request,
			{
			"title": 'Blog',
			"posts": posts, 
		 	"user" : request.user,
	 		"months" : mkmonth_lst(),
	 		"categories": category_lst(),
			"form_signup" : form,
			})
		)

def category_lst():	
	return Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')

def month(request, year, month):
	"""Monthly archive."""
	posts = Post.objects.filter(created__year=year, created__month=month)


	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')

	return render(
	request,
	'blog/list.html',
	context_instance = RequestContext(request,
		{
		"title": 'Blog by Time',
		"posts" : posts,
	 	"user": request.user,
	 	"months" : mkmonth_lst(),
 		"categories": category_lst(),
	 	"archive" : True,
		"form_signup" : form,
		})
	)



def post(request, pk):
	"""Single post with comments and a comment form."""
	post = Post.objects.get(pk=int(pk))
	comments = Comment.objects.filter(post=post)

	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')

	return render(
	request,
	'blog/post.html',
	context_instance = RequestContext(request,
		{
		"post" : post,
		"comments": comments,
		"form": CommentForm(), 
	 	"user": request.user,
 		"months" : mkmonth_lst(),
 		"categories": category_lst(),
		"form_signup" : form,
		})
	)

def add_comment(request, pk):
	""" Add a new comment. """
	p = request.POST
	if p.has_key("body") and p["body"]:
		author = "Anonymous"
		if p["author"]: author = p["author"]

		comment = Comment(post=Post.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False

		comment = cf.save(commit=False)
		comment.author = author
		
		notify = True
		if request.user.username == 'ak': notify = False
		comment.save(notify=notify)
		
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


def delete_comment(request, post_pk, pk=None):
	"""Delete comment(s) with primary key 'pk' or with pks in POST."""
	if request.user.is_staff:
		if not pk: 
			pklst = request.POST.getlist('delete')
		else: pklst = [pk]

		for pk in pklst:
			Comment.objects.get(pk=pk).delete()

		return HttpResponseRedirect(reverse("blog-post", args=(post_pk,)))

def category(request, categorySlug, pk):
	"""Get specified category"""
	posts = Post.objects.all().order_by('-created')
	category_posts = []
	for post in posts:
		if post.categories.filter(slug=categorySlug):
			category_posts.append(post)

	"""Add pagination"""
	pages = Paginator(category_posts, 5)

	"""Get the category"""
	category = Category.objects.filter(slug=categorySlug)[0]

	"""Get the specified page"""
	try:
		returned_page = pages.page(pk)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)


	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		return HttpResponseRedirect('')
		

	"""Display all the posts"""
	return render(
	request,
	'blog/category.html',
	context_instance = RequestContext(request,
		{
		"title": 'Blog by Category',
		"posts" : returned_page.object_list,
		"page": returned_page,
		"category": category, 
	 	"months" : mkmonth_lst(),
 		"categories": category_lst(),
		"form_signup" : form,
		})
	)
