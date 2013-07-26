from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        abstract = True


class Beneficiary(Person):
    is_approved = models.BooleanField(blank=True, default=False)

    class Meta(Person.Meta):
        verbose_name = "Beneficiary"
        verbose_name_plural = "Beneficiaries"


class Donor(Person):
    pass
