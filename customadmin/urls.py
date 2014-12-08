from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import approve, UnapprovedCampaigns


urlpatterns = patterns('',
                       url(r'^unapproved-campaigns/$',
                           login_required(UnapprovedCampaigns.as_view()),
                           name='unapproved'),
                       url(r'^approve/(?P<campaign_id>\d+)/$',
                           login_required(login_required(approve)),
                           name='approve'), )
