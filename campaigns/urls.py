from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from campaigns.views import create_a_campaign, CampaignDetail, CampaignsListView, CampaignUpdate, MyCampaigns


urlpatterns = patterns('',
    url(r'^$', login_required(CampaignsListView.as_view()), name='list_of_campaigns'),
    url(r'^create_a_campaign/$', login_required(create_a_campaign), name='create_a_campaign'),
    url(r'^detail/(?P<slug>[\w-]+)/$', login_required(CampaignDetail.as_view()), name='campaign_detail'),
    url(r'^edit/(?P<slug>[\w-]+)/$', login_required(CampaignUpdate.as_view()), name='edit_campaign'),
    url(r'^mycampaigns/(?P<user_id>\d+)/$', login_required(MyCampaigns.as_view()), name='my_campaigns'),
    )
