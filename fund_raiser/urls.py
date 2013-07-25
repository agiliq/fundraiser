from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.conf import settings

from authentication.views import customadmin_index, approve

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^customadmin/$', customadmin_index,
                           name='customeadmin_index'),
                       url(r'^customadmin/unapproved-users$', ListView.as_view(
                           template_name='authentication/unapproved_users.html',
                           queryset=User.objects.filter(
                           beneficiary__is_approved=False),
                           context_object_name="unapproved_users"), name='unapproved'),
                       url(r'^customadmin/approve/(?P<user_id>\d+)$',
                           approve, name='approve'),


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
