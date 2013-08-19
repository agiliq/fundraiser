# Create your views here.
import gdata.contacts.service

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from google_contacts.utils import google_get_state, google_import


def invite_gmail_contacts(request):
	request.session[settings.GOOGLE_REDIRECT_SESSION_VAR] = request.path
	google_state = google_get_state(request)
	gcs = gdata.contacts.service.ContactsService()
	google_contacts = google_import(request, gcs, cache=True)
	return render_to_response('social_feeds/gmail_contacts.html', {
		                'google_state': google_state,
		                'google_contacts': google_contacts
		                }, context_instance=RequestContext(request))
