from django.conf.urls import patterns, include, url
from fund_raiser.views import pbadmin_index, approve, create_a_campaign
from django.contrib import admin
from django.views.generic import ListView
from django.contrib.auth.models import User
from books.models import Donor, Beneficiary
from fund_raiser.models import Campaign
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include(
                           'authentication.urls', namespace='accounts')),
                       url(r'^books/', include(
                           'books.urls', namespace='books')),
                       url(r'^pbadmin/$', pbadmin_index, name='pbadmin_index'),
                       url(r'^pbadmin/unapproved-users$', ListView.as_view(
                           template_name='unapproved_users.html',
                           queryset=User.objects.filter(
                           beneficiary__approved=False),
                           context_object_name="unapproved_users"), name='unapproved'),
                       url(r'^pbadmin/approve/(?P<user_id>\d+)$',
                           approve, name='approve'),
                       url(r'^donors/$', ListView.as_view(
                           template_name='donors.html',
                           queryset=Donor.objects.all(),
                           context_object_name='donor_list'), name='list_of_donors'),
                       url(r'^beneficiaries/$', ListView.as_view(
                           template_name='beneficiaries.html',
                           queryset=Beneficiary.objects.all(),
                           context_object_name='beneficiary_list'), name='list_of_bnfs'),
                       url(r'^campaigns/$', ListView.as_view(
                           template_name='campaigns.html',
                           queryset=Campaign.objects.all(),
                           context_object_name='campaign_list'), name='list_of_campaigns'),
                       url(r'^create_a_campaign/$',
                           create_a_campaign, name='create_a_campaign'),
                       )
