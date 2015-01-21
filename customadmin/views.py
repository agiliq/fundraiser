from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.core.urlresolvers import reverse

from campaigns.models import Campaign
from profiles.tasks import sendemail


def approve(request, campaign_id):
    if request.user.is_staff:
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        campaign.is_approved = True
        campaign.save()
        # sendemail.delay(sub="approve_sub", msg="approve_msg",
        #                 to=campaign.person.user.email,
        #                 user=campaign.person.user)
        return HttpResponseRedirect(reverse('customadmin:unapproved'))
    else:
        raise Http404
    return render_to_response('unapproved_campaigns.html')


class UnapprovedCampaigns(ListView):
    template_name = 'customadmin/unapproved_campaigns.html'
    context_object_name = 'unapproved_campaigns'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404
        return super(UnapprovedCampaigns, self).get(request, *args, **kwargs)

    def get_queryset(self):
        """
        Returns the unapproved users related to person in
        the database

        """

        return Campaign.objects.filter(is_approved=False)
