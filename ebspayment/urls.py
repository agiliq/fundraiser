from django.conf.urls import url, patterns

from ebspayment.views import ebspayment, ebsresponse


urlpatterns = patterns('',
    url(r'^ebspayment/(?P<campaign_id>\d+)/$', ebspayment, name='ebsindex'), 
    url(r'^ebspayment/response', ebsresponse, name='ebsresponse'), 
)
