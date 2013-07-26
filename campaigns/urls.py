from django.conf.urls import patterns, url
from django.views.generic import ListView
from campaigns.models import Campaign
from campaigns.views import create_a_campaign


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
                           template_name='campaigns/campaigns.html',
                           queryset=Campaign.objects.all(),
                           context_object_name='campaign_list'), name='list_of_campaigns'),
    url(r'^create_a_campaign/$',create_a_campaign, name='create_a_campaign'),
    )
