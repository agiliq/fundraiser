# Create your views here.
import base64
import re
from django.shortcuts import render_to_response, get_object_or_404
# from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
# from django.core.urlresolvers import reverse

from campaigns.models import Campaign
from ebspayment.models import PaymentForm

#sample payment page
def ebspayment(request, campaign_id):
    campaign_obj = get_object_or_404(Campaign, pk=campaign_id)
    form = PaymentForm()
    if form.is_valid():
        form = PaymentForm(data=request.POST)
    return render_to_response('ebspayment/payment_form.html', {'form': form,
                                                      'campaign' : campaign_obj,
                                                      'ebs_url': settings.EBS_ACTION_URL},
                                                      context_instance=RequestContext(request))

#function to process response from EBS and decrypt
def ebsresponse(request):
    if request.method == 'GET':
	 formvalue = request.GET
         drvalue = formvalue.get('DR')
         dr = re.sub('\s','\+',drvalue) 
         data = base64.b64decode(dr)
         key = settings.EBS_SECRET_KEY
	 finalvalue = RC4(data, key)
	 params = []
         params = finalvalue.split('&')        
    	 paramdetail={}
    	 for param in params:
        	k, v = param.split('=')
        	paramdetail[k] = v
	 
    else:
	paramdetail={}	 	
    return render_to_response('ebspayment/response.html', {'response': paramdetail})

#RC4 Decryption function.Do Not edit it.
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
#Do Not Edit upto this
