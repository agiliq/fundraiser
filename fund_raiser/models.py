from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=260)
