from django.contrib import admin
from campaigns.models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('beneficiary', 'campaign_name',
                    'date_created', 'modified', 'target_amount')
    list_filter = ['beneficiary', 'campaign_name']
    search_fields = ['beneficiary', 'campaign_name']
    prepopulated_fields = {"slug": ("campaign_name",)}

admin.site.register(Campaign, CampaignAdmin)
