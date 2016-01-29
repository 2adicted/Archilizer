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
from django.contrib import admin
import django.views.defaults

urlpatterns = [
    # url(r'^$', 'archilizer.views.under_construction', name='under_construction'),
    url(r'^downloads/thankyou/$', 'archilizer.views.under_construction_subscribed', name='under_construction_subscribed'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'signup.views.home', name='home'),
    # url(r'^$', 'archilizer.views.under_construction', name='downloads'),
    url(r'^contact/$', 'signup.views.contact', name='contact'),
    url(r'^contact/thanks/$', 'signup.views.thanks', name='thanks'),
    url(r'^about/$', 'archilizer.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # training
    url(r'^training/$', 'training.views.services', name='trainings'),
    url(r'^training/(?P<pk>\d+)/$', 'training.views.module', name='module'),
    url(r'^services/$', 'training.views.services', name='services'),
    # downloads
    url(r'^downloads/$', 'archilizer.views.under_construction', name='downloads'),
    # url(r'^downloads/', 'download.views.download', name='downloads'),
    # blog
    url(r'^blog/$', 'blog.views.main', name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', 'blog.views.post', name='blog-post'),
    url(r'^blog/add_comment/(?P<pk>\d+)/$', 'blog.views.add_comment', name='blog-add-comment'),
    url(r'^blog/month/(\d+)/(\d+)/$', 'blog.views.month', name='blog-month'),
    url(r'^blog/delete_comment/(\d+)/$', 'blog.views.delete_comment', name='blog-delete-comment'),
    url(r'^blog/delete_comment/(\d+)/(\d+)/$', 'blog.views.delete_comment', name='blog-delete-comment'),
    url(r'^blog/categories/(?P<categorySlug>\w+)/?$', 'blog.views.category', name='blog-category'),
    url(r'^blog/categories/(?P<categorySlug>\w+)/(?P<pk>\d+)/?$', 'blog.views.category', name='blog-category-pk'),
    # tinymce    
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^404/$', django.views.defaults.page_not_found, ),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)