from django.contrib import admin
from campaigns.models import (
    Campaign,
    Category,
    FundDistribution,
    Reward,
    TeamMember
)


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('person', 'campaign_name',
                    'date_created', 'modified', 'target_amount')
    list_filter = ['person', 'campaign_name']
    search_fields = ['person', 'campaign_name']
    prepopulated_fields = {"slug": ("campaign_name",)}


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'short_description', 'fb_url', 'campaign']


class FundDistributionAdmin(admin.ModelAdmin):
    list_display = ['usage', 'allocation', 'campaign']


class RewardAdmin(admin.ModelAdmin):
    list_display = ['title', 'campaign']

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Category)
admin.site.register(FundDistribution, FundDistributionAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
