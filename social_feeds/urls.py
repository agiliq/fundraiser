from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from social_feeds.views import invite_gmail_contacts, send_invitation_to_gcontacts

urlpatterns = [
    url(r'^invite_gmail_contacts/$', login_required(invite_gmail_contacts), name='gmail_contacts'),
    url(r'^send_gmail_invitations/$', login_required(send_invitation_to_gcontacts), name='send_invitation_to_gcontacts'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
