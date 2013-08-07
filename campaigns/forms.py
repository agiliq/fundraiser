from django.forms import ModelForm
from campaigns.models import Campaign


class CampaignForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('beneficiary', 'slug')
