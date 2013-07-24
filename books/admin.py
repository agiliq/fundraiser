from django.contrib import admin
from books.models import Publisher, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'cost')
    list_filter = ['cost']
    search_fields = ['title', 'author', 'publisher']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'website')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
