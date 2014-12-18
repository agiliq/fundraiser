from django.forms import ModelForm
from campaigns.models import Campaign


class CampaignForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('person',
                   'slug',
                   'donation', )


class CampaignUpdateForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('slug',
                   'donation', )


class FundDistributionForm(ModelForm):

    class Meta:
        model = Campaign
