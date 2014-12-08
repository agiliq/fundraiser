from django.contrib import admin
from people.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'website')
    list_filter = ['user']
    search_fields = ['user']


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('person', 'campaign_name',
                    'date_created', 'modified', 'target_amount')
    list_filter = ['person', 'campaign_name']
    search_fields = ['person', 'campaign_name']

admin.site.register(Person, PersonAdmin)
