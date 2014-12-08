from django.contrib import admin
from campaigns.models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('person', 'campaign_name',
                    'date_created', 'modified', 'target_amount')
    list_filter = ['person', 'campaign_name']
    search_fields = ['person', 'campaign_name']
    prepopulated_fields = {"slug": ("campaign_name",)}

admin.site.register(Campaign, CampaignAdmin)
