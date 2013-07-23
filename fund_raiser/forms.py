from django import forms as newform
from django.forms import ModelForm
from fund_raiser.models import Campaign


class CampaignForm(ModelForm):

    class Meta:
        model = Campaign
        exclude = ('beneficiary', 'date_created', 'modified')
