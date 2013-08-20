from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)
    address = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=70, blank=True, unique=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:books_by_pub', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.name)
            slug_exists = True
            self.slug = slug
            counter = 1
            while slug_exists:
                try:
                    slug_exits = Publisher.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Publisher.DoesNotExist:
                    self.slug = slug
                    break
        super(Publisher, self).save(*args, **kwargs)

class Book(models.Model):
    publisher = models.ForeignKey(Publisher)
    image = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    synopsis = models.TextField(blank=True)
    cost = models.DecimalField(
        blank=True, max_digits=10, decimal_places=2, default=0.00)
    author = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.title)
            slug_exists = True
            self.slug = slug
            counter = 1
            while slug_exists:
                try:
                    slug_exits = Book.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Book.DoesNotExist:
                    self.slug = slug
                    break
        super(Book, self).save(*args, **kwargs)
