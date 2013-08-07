from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from books.models import Book
from people.models import Beneficiary


class Campaign(models.Model):
    beneficiary = models.ForeignKey(Beneficiary)
    campaign_name = models.CharField(max_length=260)
    slug = models.SlugField(max_length=150, unique=True)
    books = models.ManyToManyField(Book)
    date_created = models.DateTimeField(auto_now_add=True)
    target_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    modified = models.DateTimeField(auto_now=True)
    cause = models.TextField()

    def __unicode__(self):
        return self.campaign_name

    def get_absolute_url(self):
        return reverse('campaigns:campaign_detail', args=[self.slug])

    def get_edit_url(self):
        return reverse('campaigns:edit_campaign', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                slug = slugify(self.campaign_name)
                try:
                    obj_with_slug_exits = Campaign.objects.get(slug=slug)
                    if obj_with_slug_exits:
                        self.slug = slug + '_1'
                except Campaign.DoesNotExist:
                    self.slug = slug
        super(Campaign, self).save(*args, **kwargs)
