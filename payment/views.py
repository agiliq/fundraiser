# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
# from django.contrib import messages
# from django.core import serializers
# from django.utils import simplejson

import base64
import re
import hashlib

from campaigns.models import Campaign
from .forms import PaymentForm

from .forms import CreditCardForm
from billing import CreditCard, get_gateway


# Ebs payment gateway functions ####################

def ebspayment(request, campaign_id):
    campaign_obj = get_object_or_404(Campaign, pk=campaign_id)
    # hashstring = hashlib.md5(settings.EBS_ACCOUNT_ID+'|'+settings.EBS_SECRET_KEY).hexdigest()
    form = PaymentForm()

    # string = settings.EBS_SECRET_KEY+"|"+form.cleaned_data['account_id']+"|"
    #               +form.cleaned_data['amount']+"|"+form.cleaned_data['reference_no'] +"|"
    #               +form.cleaned_data['return_url']+"|"+form.cleaned_data['mode']
    string = settings.EBS_SECRET_KEY + "|" + '5880' + "|" + \
        '1.00' + "|" + '223' + "|" + settings.EBS_RETURN_URL + "|" + "TEST"
    print string
    secure_hash = hashlib.md5(string).hexdigest()
    return render_to_response('payment/payment_form.html', {'form': form,
                                                            'campaign': campaign_obj,
                                                            'ebs_url': settings.EBS_ACTION_URL,
                                                            'secure_hash': secure_hash},
                              context_instance=RequestContext(request))

# function to process response from EBS and decrypt


def ebsresponse(request):
    if request.method == 'GET':
        formvalue = request.GET
        drvalue = formvalue.get('DR')
        dr = re.sub('\s', '\+', drvalue)
        data = base64.b64decode(dr)
        key = settings.EBS_SECRET_KEY
        finalvalue = RC4(data, key)
        params = []
        params = finalvalue.split('&')
        paramdetail = {}
        for param in params:
            k, v = param.split('=')
            paramdetail[k] = v

    else:
        paramdetail = {}
    return render_to_response('payment/response.html', {'response': paramdetail})

# RC4 Decryption function.Do Not edit it.


def RC4(data, key):
    x = 0
    s = range(256)
    for i in range(256):
        x = (x + s[i] + ord(key[i % len(key)])) % 256
        s[i], s[x] = s[x], s[i]
    x = y = 0
    out = ""
    for c in data:
        x = (x + 1) % 256
        y = (y + s[x]) % 256
        s[x], s[y] = s[y], s[x]
        out += chr(ord(c) ^ s[(s[x] + s[y]) % 256])
    return out
# Do Not Edit upto this

# Stripe payment gateway functions ####################


def stripepayment(request,  campaign_id):
    campaign_obj = get_object_or_404(Campaign, pk=campaign_id)
    amount = int(campaign_obj.target_amount)
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data
            credit_card = CreditCard(**data)
            merchant = get_gateway("stripe")
            response = merchant.purchase(amount, credit_card)
            response_dict = {}
            response_dict.update({'status': response['status']})
            response_dict.update(response['response'])
            del response_dict['card']
            response_dict.update(response['response']['card'])
            request.session['response'] = response_dict
            return HttpResponseRedirect(reverse('paygate:payment_success', args=[campaign_id]))
    else:
        form = CreditCardForm(initial={'number': '4242424242424242'})
    return render_to_response(
        'payment/stripe_payment_form.html', {'form': form,
                                             'campaign': campaign_obj},
        context_instance=RequestContext(request))


class PaymentSuccess(TemplateView):
    template_name = 'payment/payment_success.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentSuccess, self).get_context_data(**kwargs)
        context['response'] = self.request.session['response']
        return context
