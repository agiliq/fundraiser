"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from books.models import Book, Publisher


class BooksAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")
        self.publisher = Publisher.objects.create(
            name='bsp', slug='bsp', address='address')
        self.book = Book.objects.create(publisher=self.publisher,
                                        image='/home/agiliq/Desktop/screenshots/gradmale_avatar.png',
                                        title='title', slug='slug', author='author', cost='40.0')

    def test_BooksListView(self):
        response = self.c.get(reverse("books:listofbooks"))
        self.assertEqual(200, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("books:publishers"))
        self.assertEqual(200, response.status_code)

    def test_BooksDetailView(self):
        response = self.c.get(reverse("books:book_detail", args=['arg']))
        self.assertEqual(404, response.status_code)
        response = self.c.get(reverse("books:book_detail", args=[
                              self.book.slug]))
        self.assertEqual(200, response.status_code)

    def test_PublishersListView(self):
        response = self.c.get(reverse("books:listofbooks"))
        self.assertEqual(200, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("books:publishers"))
        self.assertEqual(200, response.status_code)

    def test_PublishersDetailView(self):
        response = self.c.get(reverse("books:books_by_pub", args=['arg']))
        self.assertEqual(200, response.status_code)
        response = self.c.get(reverse("books:books_by_pub", args=[
                              self.publisher.slug]))
        self.assertEqual(200, response.status_code)


class ModelTests(TestCase):

    def setUp(self):
        self.publisher = create_publisher()
        pass

    def test_create_publisher(self):
        for i in range(3):
            Publisher.objects.create(name='pub', email='{0}@gmail.com'.format(i))

    def test_create_book(self):
        for i in range(3):
            Book.objects.create(publisher=self.publisher, title='abc')


def create_publisher():
    return Publisher.objects.create(name='test')
