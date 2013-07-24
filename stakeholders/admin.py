from django.contrib import admin
from stakeholders.models import Beneficiary, Donor, Campaign


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'website', 'is_approved')
    list_filter = ['user', 'is_approved']
    search_fields = ['user', 'is_approved']


class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'website')
    list_filter = ['user']
    search_fields = ['user']


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('beneficiary', 'campaign_name',
                    'date_created', 'modified', 'target_amount')
    list_filter = ['beneficiary', 'campaign_name']
    search_fields = ['beneficiary', 'campaign_name']

admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Campaign, CampaignAdmin)
