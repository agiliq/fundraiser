from django.db import models
from django.contrib.auth.models import User
from books.models import Book


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


class Campaign(models.Model):
    beneficiary = models.ForeignKey(Beneficiary)
    campaign_name = models.CharField(max_length=260)
    books = models.ManyToManyField(Book)
    date_created = models.DateTimeField(auto_now_add=True)
    target_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    modified = models.DateTimeField(auto_now=True)
    cause = models.TextField()

    def __unicode__(self):
        return self.campaign_name
