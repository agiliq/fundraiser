from django.conf.urls import patterns, url

from campaigns.views import create_a_campaign, CampaignDetail, CampaignsListView, CampaignUpdate, MyCampaigns


urlpatterns = patterns('',
    url(r'^$', CampaignsListView.as_view(), name='list_of_campaigns'),
    url(r'^create_a_campaign/$',create_a_campaign, name='create_a_campaign'),
    url(r'^campaign/detail/(?P<pk>\d+)/$',CampaignDetail.as_view(), name='campaign_detail'),
    url(r'^campaign/edit/(?P<pk>\d+)/$',CampaignUpdate.as_view(), name='edit_campaign'),    
    url(r'^mycampaigns/(?P<user_id>\d+)/$',MyCampaigns.as_view(), name='my_campaigns'),    
    )
