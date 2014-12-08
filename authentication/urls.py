from django.conf.urls import patterns, url

from .views import user_login, user_logout
from .views import PersonRegistrationView


urlpatterns = patterns('',
                       url(r'^register/person$',
                           PersonRegistrationView.as_view(), name='person'),
                       url(r'^login/$', user_login, name='login'),
                       url(r'^logout/$', user_logout, name='logout'))
