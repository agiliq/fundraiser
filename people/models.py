from django.db import models
from django.contrib.auth.models import User


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
