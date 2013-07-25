from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name


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
