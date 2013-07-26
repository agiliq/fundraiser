from django.conf.urls import patterns, url
from django.views.generic import ListView
from people.models import Donor, Beneficiary


urlpatterns = patterns('',
                       url(r'^beneficiaries/$', ListView.as_view(
                           template_name='people/beneficiaries.html',
                           queryset=Beneficiary.objects.all(),
                           context_object_name='beneficiary_list'), name='list_of_bnfs'),
                       url(r'^donors/$', ListView.as_view(
                           template_name='people/donors.html',
                           queryset=Donor.objects.all(),
                           context_object_name='donor_list'), name='list_of_donors'),
                       )
