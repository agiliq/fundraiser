"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import (
    Category,
    Campaign,
    FundDistribution,
    Reward,
    TeamMember, )
from people.models import Person


class CampaignsAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")
        self.cam_user1 = Person.objects.create(
            user=User.objects.create_user(
                username='test1', email='test1@agiliq.com', password='test1'),
            address='101, test apt, testville',
            website='http://www.testone.com')
        self.cam_user2 = Person.objects.create(
            user=User.objects.create_user(
                username='test2', email='test2@agiliq.com', password='test2'),
            address='102, test apt, testville',
            website='http://www.testtwo.com')

    def test_create_a_campaign_view(self):
        response = self.c.get(reverse("campaigns:create_a_campaign"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("campaigns:create_a_campaign"))
        self.assertEqual(200, response.status_code)

    def test_MycampaignsView(self):
        response = self.c.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(200, response.status_code)

    def test_testpay(self):
        response = self.c.get(
            reverse("campaigns:testpay", args=[self.user.id]))

        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")

        response = self.c.get(
            reverse("campaigns:testpay", args=[self.user.id]))

        self.assertEqual(200, response.status_code)

    def test_can_create_and_retrive_categories(self):
        first = Category.objects.create(name='test one')
        second = Category.objects.create(name='test two')

        self.assertEqual(Category.objects.count(), 2)

    def test_campaign_are_added_to_right_category(self):
        self.categories = ['App', 'Art']
        for each in self.categories:
            Category.objects.create(name=each)
        cam_obj1 = Campaign.objects.create(
            person=self.cam_user1,
            category=Category.objects.get(name='Art'),
            campaign_name='Campaign One')
        cam_obj2 = Campaign.objects.create(
            person=self.cam_user2,
            category=Category.objects.get(name='App'),
            campaign_name='Campaign Two')
        cat_art = Category.objects.get(name='Art')
        cat_app = Category.objects.get(name='App')

        self.assertEqual(cat_art.campaign_set.count(), 1)
        self.assertEqual(cat_app.campaign_set.count(), 1)
        self.assertEqual(
            cat_art.campaign_set.all()[0].campaign_name, 'Campaign One')
        self.assertEqual(
            cat_app.campaign_set.all()[0].campaign_name, 'Campaign Two')

    def test_user_can_create_multiple_campaigns(self):
        cam_obj1 = Campaign.objects.create(
            person=self.cam_user1, campaign_name='Campaign 1',
            category=Category.objects.create())
        cam_obj2 = Campaign.objects.create(
            person=self.cam_user1, campaign_name='Campaign 2',
            category=Category.objects.create())

        self.assertEqual(self.cam_user1.campaign_set.count(), 2)
