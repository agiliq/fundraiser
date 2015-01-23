"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import (
    Category,
    Campaign,
    FundDistribution,
    Reward,
    TeamMember, )
from people.models import Person


class CampaignUnauthorizedRedirectsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")

    def test_create_a_campaign_view(self):
        response = self.client.get(reverse("campaigns:create_a_campaign"))
        self.assertEqual(302, response.status_code)
        self.client.login(username="admin", password="admin")
        response = self.client.get(reverse("campaigns:create_a_campaign"))
        self.assertEqual(200, response.status_code)

    def test_MycampaignsView(self):
        response = self.client.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(302, response.status_code)
        self.client.login(username="admin", password="admin")
        response = self.client.get(
            reverse("campaigns:my_campaigns", args=[self.user.id]))
        self.assertEqual(200, response.status_code)

    def test_testpay(self):
        response = self.client.get(
            reverse("campaigns:testpay", args=[self.user.id]))
        self.assertEqual(302, response.status_code)
        self.client.login(username="admin", password="admin")
        response = self.client.get(
            reverse("campaigns:testpay", args=[self.user.id]))
        self.assertEqual(200, response.status_code)


class CampaignsViewTestCase(TestCase):

    def setUp(self):
        Person.objects.create(user=User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin"),
            address='Address apt', website='www.webworld.com')
        self.categories = ['App', 'Music', 'Art', 'Technology', 'Publishing']
        for each in self.categories:
            Category.objects.create(name=each)

    def post_campaign(self, **kwargs ):
        self.client.post(
            '/create_a_campaign/',
            data={'category': kwargs['cat'],
                  'campaign_name': kwargs['cam_name'],
                  'target_amount': '4500',
                  'cause': 'No Cause', })

    def login(self):
        self.client.post(
            '/accounts/login/',
            data={'username': 'admin',
                  'password': 'admin'})

    def approve(self, cam_obj):
        cam_obj.is_approved = True
        cam_obj.save()

    def test_user_can_create_campaign(self):
        self.login()
        self.post_campaign(cat=3, cam_name='Campaign one')

        self.assertEqual(Campaign.objects.count(), 1)

    def test_campaign_belongs_to_correct_category(self):
        self.login()
        self.post_campaign(cat=1, cam_name='Campaign One')
        cam_obj = Campaign.objects.all()[0]
        self.approve(cam_obj)

        response = self.client.get(
            reverse('campaigns:category_detail', args=(
                Category.objects.get(name=self.categories[0]).id, )))

        self.assertContains(response, cam_obj.campaign_name)

    def test_only_approved_campaigns_appear_at_homepage(self):
        self.login()
        self.post_campaign(cat=4, cam_name='Campaign One')
        approved_cam_obj = Campaign.objects.get(campaign_name='Campaign One')
        self.approve(approved_cam_obj)

        response = self.client.get(
            reverse('campaigns:list_of_campaigns'))

        self.assertContains(response, approved_cam_obj.campaign_name)

    def test_unapproved_campaigns_does_not_public(self):
        self.login()
        self.post_campaign(cat=1, cam_name='Campaign Two')
        unapproved_cam_obj = Campaign.objects.get(campaign_name='Campaign Two')

        response = self.client.get(
            reverse('campaigns:list_of_campaigns'))

        self.assertNotContains(response, unapproved_cam_obj.campaign_name)

    def test_campaign_detail_are_correct(self):
        self.login()
        self.post_campaign(cat=3, cam_name='Campaign One')
        cam_obj = Campaign.objects.all()[0]
        self.approve(cam_obj)

        response = self.client.get(
            reverse('campaigns:campaign_detail', args=(cam_obj.slug, )))
        for each in [cam_obj.person.user.username.capitalize(),
                     cam_obj.category.name,
                     cam_obj.campaign_name,
                     cam_obj.target_amount.to_eng_string(),
                     cam_obj.cause]:
            self.assertIn(each, response.content.decode())
