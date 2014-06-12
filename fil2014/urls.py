from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exhibitors/', include('exhibitors.urls')),
    # Examples:
    # url(r'^$', 'fil2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^libros/', 'exhibitors.views.books'),
    url(r'^expositores-y-conferencias/', 'presentations.views.presentations'),
    url(r'^talleres/', 'exhibitors.views.workshops'),
    url(r'^otros/', 'exhibitors.views.others'),
    url(r'^$', 'exhibitors.views.books'),
)
