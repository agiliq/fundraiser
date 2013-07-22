from django.contrib import admin
from books.models import Publisher, Book, Beneficiary, Donor


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'cost')
    list_filter = ['cost']
    search_fields = ['title', 'author', 'publisher']
    date_hierarchy = 'publication_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'country', 'phone', 'email', 'website')
    list_filter = ['name']
    search_fields = ['name', 'country']


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('beneficiary_name', 'ben_type',
                    'address', 'country', 'phone', 'email', 'website', 'approved')
    list_filter = ['beneficiary_name', 'ben_type', 'approved']
    search_fields = ['beneficiary_name', 'country', 'approved']


class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_user', 'address', 'country', 'phone', 'email')
    list_filter = ['donor_user']
    search_fields = ['donor_user', 'country']

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Donor, DonorAdmin)
