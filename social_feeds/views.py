# Create your views here.
import gdata.contacts.service

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from profiles.tasks import massemail
from contacts.utils import google_get_state, google_import


def invite_gmail_contacts(request):
    request.session[settings.GOOGLE_REDIRECT_SESSION_VAR] = request.path
    google_state = google_get_state(request)
    gcs = gdata.contacts.service.ContactsService()
    google_contacts = google_import(request, gcs, cache=True)
    filtered_contacts = []
    if 'q' in request.GET and request.GET['q']:
        search_string = request.GET.get('q', None)
        filtered_contacts = [contact.decode('utf-8')
                             for contact in google_contacts if search_string in contact.decode('utf-8')]
    if filtered_contacts:
        return render_to_response('social_feeds/gmail_contacts.html', {
            'google_state': google_state,
            'google_contacts': filtered_contacts,
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('social_feeds/gmail_contacts.html', {
            'google_state': google_state,
            'google_contacts': google_contacts,
            'filtered_contacts': filtered_contacts
        }, context_instance=RequestContext(request))


def send_invitation_to_gcontacts(request):
    error = True
    if request.method == 'POST':
        if 'invite' in request.POST:
            error = False
            email_list = request.POST.getlist('invite')
            massemail.delay(
                'gmail_invite', 'gm_invite_msg', email_list, request.user)
            messages.add_message(
                request, messages.SUCCESS, 'Your invitations has been sent to the selected users !!!!')
            # return HttpResponseRedirect(reverse('index:home'))
        else:
            error = True
    return render_to_response('social_feeds/invitations_sent.html', {'error': error}, context_instance=RequestContext(request))
