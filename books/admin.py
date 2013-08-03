from django.contrib import admin
from books.models import Publisher, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'cost')
    list_filter = ['title', 'cost']
    search_fields = ['title', 'author', 'publisher__name']
    prepopulated_fields = {"slug": ("title",)}


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'website')
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
