from books.models import Book
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
