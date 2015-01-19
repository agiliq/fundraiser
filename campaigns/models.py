from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from people.models import Person


class Category(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories:category_detail', args=[self.id])

    def approved_campaigns(self):
        return self.campaign_set.filter(is_approved=True)


# class Questionaire(models.Model):
#
#     pass


class Campaign(models.Model):
    person = models.ForeignKey(Person)
    category = models.ForeignKey(Category)
    campaign_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    target_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    modified = models.DateTimeField(auto_now=True)
    cause = models.TextField()
    image = models.ImageField(upload_to="campaign_covers/",
                              blank=True, null=True)
    is_approved = models.BooleanField(blank=True, default=False)
    donation = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

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


class TeamMember(models.Model):

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400)
    fb_url = models.URLField()
    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return self.name


class Reward(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return self.title


class FundDistribution(models.Model):

    usage = models.CharField(max_length=200)
    allocation = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return self.usage
