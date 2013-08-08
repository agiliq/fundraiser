"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class CustomAdminTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")

    def test_indexView(self):
        response = self.c.get(reverse("customadmin:customadmin_index"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("customadmin:customadmin_index"))
        self.assertEqual(200, response.status_code)

    def test_unapprovedusers(self):
        response = self.c.get(reverse("customadmin:unapproved"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("customadmin:unapproved"))
        self.assertEqual(200, response.status_code)

