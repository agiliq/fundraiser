from django.db import models
from django.core.urlresolvers import reverse

from books.models import Book
from people.models import Beneficiary


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

    def get_absolute_url(self):
        return reverse('campaigns:campaign_detail', args=[self.id])

    def get_edit_url(self):
        return reverse('campaigns:edit_campaign', args=[self.id])