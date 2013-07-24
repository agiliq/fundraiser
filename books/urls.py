from django.conf.urls import patterns, url
from books import views
from django.views.generic import ListView
from books.models import Publisher


urlpatterns = patterns('',
                       url(r'^$', views.BooksList, name='listofbooks'),
                       url(r'^publishers$', views.BooksList, name='listofbooks'),
                       url(r'^publishers/$', ListView.as_view(
                           template_name='books/publishers.html',
                           queryset=Publisher.objects.all(),
                           context_object_name='publisher_list'), name='publishers'),
                       url(r'^publishers/(?P<pub_id>\d+)$', views.books_by_pub, name='books_by_pub'),

                       )
