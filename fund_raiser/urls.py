from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('books.urls', namespace='index')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^customadmin/', include('customadmin.urls', namespace='customadmin')),


    url(r'^accounts/', include('authentication.urls', namespace='accounts')),


    url(r'^', include('books.urls', namespace='books')),

    url(r'^people/', include('people.urls', namespace='people')),

    url(r'^campaigns/', include('campaigns.urls', namespace='campaigns')),

    url(r'^', include('payment.urls', namespace='paygate')),
    
    url(r'^', include('social_feeds.urls', namespace='social')),

    url(r'^', include('contacts.urls', namespace='contacts')),
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
