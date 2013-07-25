from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^customadmin/', include(
                           'authentication.urls', namespace='customadmin')),


                       url(r'^accounts/', include(
                           'authentication.urls', namespace='accounts')),


                       url(r'^books/', include(
                           'books.urls', namespace='books')),

                       url(r'^people/', include(
                           'people.urls', namespace='people')),

                       url(r'^campaigns/', include(
                           'campaigns.urls', namespace='campaigns')),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
                            )
