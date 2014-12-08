from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from campaigns import views


urlpatterns = patterns('',
                       url(r'^$', views.CampaignsListView.as_view(),
                           name='list_of_campaigns'),
                       url(r'^create_a_campaign/$',
                           login_required(views.create_a_campaign),
                           name='create_a_campaign'),
                       url(r'^detail/(?P<slug>[\w-]+)/$',
                           views.CampaignDetail.as_view(),
                           name='campaign_detail'),
                       url(r'^edit/(?P<slug>[\w-]+)/$',
                           login_required(views.CampaignUpdate.as_view()),
                           name='edit_campaign'),
                       url(r'^mycampaigns/(?P<user_id>\d+)/$',
                           login_required(views.MyCampaigns.as_view()),
                           name='my_campaigns'),
                       url(r'^test_payment/(?P<campaign_id>\d+)$',
                           login_required(views.testpay), name='testpay'), )
