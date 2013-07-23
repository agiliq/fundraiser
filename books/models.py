from django.db import models
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to="book_covers/")
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True)
    cost = models.DecimalField(blank=True, max_digits=10, decimal_places=2, default=0.00)
    author = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Beneficiary(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)
    is_approved = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Beneficiary"
        verbose_name_plural = "Beneficiaries"

    def __unicode__(self):
        return self.user.username


class Donor(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.user.username)
