from django.contrib import admin
from fund_raiser.models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'date_created', 'modified', 'target_amount')
    list_filter = ['campaign_name', 'date_created', 'target_amount']
    search_fields = ['campaign_name']
    date_hierarchy = 'date_created'
    readonly_fields = ("date_created", "modified")


admin.site.register(Campaign, CampaignAdmin)
