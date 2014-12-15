from django.forms import ModelForm
from campaigns.models import Campaign


class CampaignForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('person',
                   'slug',
                   'donation',
                   'rewards',
                   'fund_distribution')


class CampaignUpdateForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('slug',
                   'donation',
                   'rewards',
                   'fund_distribution')
