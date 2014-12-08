from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required

from .views import ebspayment, ebsresponse, stripepayment


urlpatterns = patterns('',
                       url(r'^ebspayment/(?P<campaign_id>\d+)/$',
                           login_required(ebspayment), name='ebsindex'),
                       url(r'^ebspayment/response',
                           login_required(ebsresponse),
                           name='ebsresponse'),
                       url(r'^stripe/(?P<campaign_id>\d+)/$',
                           stripepayment, name='stripeindex'),
                       url(r'^success/(?P<campaign_id>\d+)/$',
                           PaymentSuccess.as_view(),
                           name='payment_success'),
                       url(r'^payment/success/$',
                           PaymentSuccess,
                           name='payment_success'), )
