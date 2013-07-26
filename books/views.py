from books.models import Book
from django.views import generic
from django.shortcuts import render_to_response
from books.models import Book
from django.template import RequestContext
from django.views import generic


class BooksListView(generic.ListView):
    template_name = 'books/list_of_books.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        # """Return the last five published polls."""
        # return Poll.objects.order_by('-pub_date')[:5]
        """
        Returns the available books in the database
        """
        return Book.objects.all()

BooksList = BooksListView.as_view()


def books_by_pub(request, pub_id, slug):
    books_by_pub = Book.objects.filter(publisher__id=pub_id)
    return render_to_response('books/books_by_pub.html', {'books_by_pub': books_by_pub}, context_instance=RequestContext(request))


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/books_desc.html'
    context_object_name = 'book'
