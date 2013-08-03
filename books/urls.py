from django.conf.urls import patterns, url

from .views import BookDetail, BooksbyPubView, PublishersListView, BooksListView


urlpatterns = patterns('',
   url(r'^$', BooksListView.as_view(), name='listofbooks'),
   url(r'^books/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', BookDetail.as_view(), name='book_detail'),
   url(r'^publishers/$', PublishersListView.as_view(), name='publishers'),
   url(r'^publishers/(?P<pub_id>\d+)/(?P<slug>[\w-]+)/$', BooksbyPubView.as_view(), name='books_by_pub'),
)
