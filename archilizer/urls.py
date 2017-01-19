"""archilizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.http import HttpResponse
import django.views.defaults

from blog.models import LatestNewsFeed

from views import BlogSitemap, StaticViewSitemap

from archilizer import views as archilizer_views
from signup import views as signup_views
from training import views as training_views
from release import views as release_views
from blog import views as blog_views

sitemaps = {
'post' : BlogSitemap,
'static' : StaticViewSitemap,        
}

urlpatterns = [
    # url(r'^$', 'archilizer.views.under_construction', name='under_construction'),
    url(r'^downloads/thankyou/$', archilizer_views.under_construction_subscribed, name='under_construction_subscribed'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', signup_views.home, name='home'),
    # url(r'^$', 'archilizer.views.under_construction', name='downloads'),
    url(r'^contact/$', signup_views.contact, name='contact'),
    url(r'^contact/thanks/$', signup_views.thanks, name='thanks'),
    url(r'^about/$', archilizer_views.about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # training
    url(r'^training/$', training_views.services, name='trainings'),
    url(r'^training/(?P<pk>\d+)/$', training_views.module, name='module'),
    url(r'^services/$', training_views.services, name='services'),
    # downloads
    url(r'^downloads/$', archilizer_views.under_construction, name='downloads'),
    # url(r'^downloads/', 'download.views.download', name='downloads'),
    url(r'^donate$', archilizer_views.donate, name='donate'),
    url(r'^stripe/donation', archilizer_views.stripe_donation),
    # release
    url(r'^release/$', release_views.main, name='release'),
    # blog
    url(r'^blog/$', blog_views.main, name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', blog_views.post, name='blog-post'),
    url(r'^blog/(?P<slug>[\w-]+)/$', blog_views.post_detail, name='blog-detail'),
    url(r'^blog/add_comment/(?P<pk>\d+)/$', blog_views.add_comment, name='blog-add-comment'),
    url(r'^blog/month/(\d+)/(\d+)/$', blog_views.month, name='blog-month'),
    url(r'^blog/delete_comment/(\d+)/$', blog_views.delete_comment, name='blog-delete-comment'),
    url(r'^blog/delete_comment/(\d+)/(\d+)/$', blog_views.delete_comment, name='blog-delete-comment'),
    url(r'^blog/categories/(?P<categorySlug>\w+)/?$', blog_views.category, name='blog-category'),
    url(r'^blog/categories/(?P<categorySlug>\w+)/(?P<pk>\d+)/?$', blog_views.category, name='blog-category-pk'),
    # tinymce    
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^404/$', django.views.defaults.page_not_found, ),
    # feed
    url(r'^latest/feed/$', LatestNewsFeed()),
    # verification
    url(r'^googlea3bd852d82023258\.html$', lambda r: HttpResponse("google-site-verification: googlea3bd852d82023258.html", content_type="text/plain")),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain")),
    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)