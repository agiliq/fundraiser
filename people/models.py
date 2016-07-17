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
        if self.user.profile.is_beneficiary:
            return reverse('people:beneficiary_detail', args=[self.id])
        else:
            return reverse('people:donor_detail', args=[self.id])

    class Meta:
        abstract = True


class Beneficiary(Person):
    is_approved = models.BooleanField(blank=True, default=False)

    class Meta(Person.Meta):
        verbose_name = "Beneficiary"
        verbose_name_plural = "Beneficiaries"


class Donor(Person):
    pass
