from django.views import generic

from .models import Book, Publisher


class BooksListView(generic.ListView):
    model = Book
    template_name = 'books/list_of_books.html'
    context_object_name = 'list_of_books'
    paginate_by = 10



class BooksbyPubView(generic.ListView):
    template_name = 'books/books_by_pub.html'
    context_object_name = 'books_by_pub'
    paginate_by = 10

    def get_queryset(self):
        """
        Returns the available books by the publisher in the database
        """
        return Book.objects.filter(publisher__id=self.kwargs['pub_id'])


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/books_desc.html'
    context_object_name = 'book'


class PublishersListView(generic.ListView):
    model = Publisher
    template_name = 'books/publishers.html'
    context_object_name = 'publisher_list'
    paginate_by = 10

