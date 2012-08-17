from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template
from books.views import manage_authors_formset, manage_authors_form

from books.api import AuthorResource
from tastypie.api import Api
from django.conf.urls.defaults import *



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#author_resource = AuthorResource()
v1_api = Api(api_name='v1')
v1_api.register(AuthorResource())
author_resource = AuthorResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^manage_authors_formset/$', manage_authors_formset),
    (r'^manage_authors_form/$', manage_authors_form),
    (r'^manage_authors_form/thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^api/', include(author_resource.urls)),
    (r'^css/style.css$', direct_to_template, {'template': 'css/style.css'}),
)

