from django.conf.urls import patterns, url
from authentication.views import register


urlpatterns = patterns('',
                       url(r'^register/donor$', register, name='donor'),
                       url(r'^register/beneficiary$',register, name='beneficiary'),
                       )
