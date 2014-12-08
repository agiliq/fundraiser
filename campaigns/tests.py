"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class CampaignsAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")

    def test_CampaignsListView(self):
        response = self.c.get(reverse("campaigns:list_of_campaigns"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("campaigns:list_of_campaigns"))
        self.assertEqual(200, response.status_code)

    def test_MycampaignsView(self):
        response = self.c.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(200, response.status_code)
