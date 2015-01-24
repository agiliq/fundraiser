"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.http import HttpRequest

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
        data={}
        for each in kwargs.keys():
            if each not in ['category',
                            'campaign_name',
                            'target_amount',
                            'cause']:
                data[each.replace('_','-')] = kwargs[each]
            else:
                data[each] = kwargs[each]
        #import ipdb; ipdb.set_trace()
        self.client.post('/create_a_campaign/', data=data)

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
        self.post_campaign(category=3, campaign_name='Campaign one',
                           target_amount=4500,
                           cause='No cause',
                           fund_dist_desc1='First',
                           fund_dist_amt1=2000,
                           fund_dist_desc2='Second',
                           fund_dist_amt2=2500,
                           reward1='R1',
                           reward2='R2',
                           name1='Admin',
                           role1='Admin',
                           short_description1='Admin',
                           fb_url1='Admin',
                           name2='admin_2',
                           role2='dy. admin',
                           short_description2='Deputy to admin',
                           fb_url2='dy.admin', )

        self.assertEqual(Campaign.objects.count(), 1)
        self.assertEqual(FundDistribution.objects.count(), 2)
        self.assertEqual(Reward.objects.count(), 2)
        self.assertEqual(TeamMember.objects.count(), 2)

    def test_campaign_belongs_to_correct_category(self):
        self.login()
        self.post_campaign(category=1, campaign_name='Campaign One',
                           target_amount=4500,
                           cause='No cause', )
        cam_obj = Campaign.objects.all()[0]
        self.approve(cam_obj)

        response = self.client.get(
            reverse('campaigns:category_detail', args=(
                Category.objects.get(name=self.categories[0]).id, )))

        self.assertContains(response, cam_obj.campaign_name)

    def test_only_approved_campaigns_appear_at_homepage(self):
        self.login()
        self.post_campaign(category=4, campaign_name='Campaign One',
                           target_amount=4500,
                           cause='No cause', )
        approved_cam_obj = Campaign.objects.get(campaign_name='Campaign One')
        self.approve(approved_cam_obj)

        response = self.client.get(
            reverse('campaigns:list_of_campaigns'))

        self.assertContains(response, approved_cam_obj.campaign_name)

    def test_unapproved_campaigns_are_not_public(self):
        self.login()
        self.post_campaign(category=1, campaign_name='Campaign Two',
                           target_amount=4500,
                           cause='No cause', )
        unapproved_cam_obj = Campaign.objects.get(campaign_name='Campaign Two')

        response = self.client.get(
            reverse('campaigns:list_of_campaigns'))

        self.assertNotContains(response, unapproved_cam_obj.campaign_name)

    def test_campaign_detail_are_correct(self):
        self.login()
        self.post_campaign(category=3, campaign_name='Campaign One',
                           target_amount=4500,
                           cause='No cause',
                           fund_dist_desc1='First',
                           fund_dist_amt1=2000,
                           fund_dist_desc2='Second',
                           fund_dist_amt2=2500,
                           reward1='R1',
                           reward2='R2',
                           name1='Admin',
                           role1='Admin',
                           short_description1='Admin',
                           fb_url1='Admin',
                           name2='admin_2',
                           role2='dy. admin',
                           short_description2='Deputy to admin',
                           fb_url2='dy.admin', )
        cam_obj = Campaign.objects.all()[0]
        self.approve(cam_obj)

        response = self.client.get(
            reverse('campaigns:campaign_detail', args=(cam_obj.slug, )))
        expected_html = render_to_string('campaigns/campaign_detail.html',
                                         {'campaign':cam_obj, })
        import ipdb; ipdb.set_trace()
        self.assertEqual(response.content.decode(), expected_html)
