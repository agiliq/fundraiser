from django.conf.urls import url, patterns

from .views import ebspayment, ebsresponse, stripepayment, PaymentSuccess


urlpatterns = patterns('',
    url(r'^ebspayment/(?P<campaign_id>\d+)/$', ebspayment, name='ebsindex'),
    url(r'^ebspayment/response', ebsresponse, name='ebsresponse'),

    url(r'^payment/stripe/(?P<campaign_id>\d+)/$', stripepayment, name='stripeindex'),
    url(r'^payment/success/$', PaymentSuccess.as_view(), name='payment_success'),
)
