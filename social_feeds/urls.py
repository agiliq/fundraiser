from django.conf.urls import patterns,  url
from django.conf import settings
from django.conf.urls.static import static

from social_feeds.views import invite_gmail_contacts

urlpatterns = patterns('',
    url(r'^invite_gmail_contacts/$', invite_gmail_contacts, name='gmail_contacts'),
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
