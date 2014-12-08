from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Person(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=150)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('people:person_detail', args=[self.id])
