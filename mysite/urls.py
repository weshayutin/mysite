from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template

from mysite.views import hello, current_datetime, hours_ahead
from books.views import search_form, search, add, manage_authors
from contact.views import contact
from mysite.views import display_meta
from ajaxContact.views import contact_form



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^hello/(.*)/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^meta/$', display_meta),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
    (r'^add/$', manage_authors),
    (r'^contact_old/$', contact),
)

'''
urlpatterns = patterns('ajaxContact.views',
    url(r'^contact/$', contact_form, name="contact_form"),
    url(r'^contact/success/$', direct_to_template, {'template': 'contact/thanks.html'},
        name="contact_success"),
)
'''