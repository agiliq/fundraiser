from django.db import models
from django.contrib.auth.models import User


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    publisher = models.ForeignKey(Publisher)
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True)
    cost = models.IntegerField(blank=True, default=0.0)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Beneficiary(models.Model):
    beneficiary_user = models.OneToOneField(User)
    beneficiary_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    ben_type = models.CharField(max_length=100, verbose_name='Type')
    strength = models.IntegerField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    approved = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Beneficiary"
        verbose_name_plural = "Beneficiaries"

    def __unicode__(self):
        return self.beneficiary_name


class Donor(models.Model):
    donor_user = models.OneToOneField(User)
    email = models.EmailField(max_length=70, unique=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"

    def __unicode__(self):
        return "{0}".format(self.donor_user)
