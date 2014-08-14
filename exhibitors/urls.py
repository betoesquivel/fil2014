from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^libros/$', 'exhibitors.views.books'),
    url(r'^libros/busqueda/$', 'exhibitors.views.getBooks'),
    url(r'^libros/busquedaFeria/$', 'exhibitors.views.getDbBooks'),
    url(r'^libros/busquedaGoogle/$', 'exhibitors.views.getGoogleBooks'),
   # url(r'^talleres/$', 'exhibitors.views.workshops'),
   # url(r'^otros/$', 'exhibitors.views.exhibitors'),
)
