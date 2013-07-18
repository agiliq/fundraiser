from django.db import models


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


class Books(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True)
    cost = models.IntegerField(blank=True, default=0.0)
    author = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title
