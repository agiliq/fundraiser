from books.models import Book
from django.views import generic
from django.shortcuts import render_to_response
from books.models import Book
from django.template import RequestContext
from django.views import generic


class BooksListView(generic.ListView):
    template_name = 'books/list_of_books.html'
    context_object_name = 'list_of_books'
    paginate_by = 1

    def get_queryset(self):
        """
        Returns the available books in the database
        """
        return Book.objects.all()

BooksList = BooksListView.as_view()


class BooksbyPubView(generic.ListView):
    template_name = 'books/books_by_pub.html'
    context_object_name = 'books_by_pub'
    paginate_by = 1

    def get_queryset(self):
        """
        Returns the available books by the publisher in the database
        """
        return Book.objects.filter(publisher__id=self.kwargs['pub_id'])

class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/books_desc.html'
    context_object_name = 'book'
