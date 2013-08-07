from django.conf.urls import patterns, url

from .views import BookDetail, BooksbyPubView, PublishersListView, BooksListView


urlpatterns = patterns('',
   url(r'^$', BooksListView.as_view(), name='listofbooks'),
   url(r'^book/(?P<slug>[\w-]+)/$', BookDetail.as_view(), name='book_detail'),
   url(r'^publishers/$', PublishersListView.as_view(), name='publishers'),
   url(r'^publishers/(?P<slug>[\w-]+)/$', BooksbyPubView.as_view(), name='books_by_pub'),
)
