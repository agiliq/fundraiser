from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import approve, UnapprovedUsers, CustomAdminIndex


urlpatterns = patterns('',
   url(r'^$', CustomAdminIndex.as_view(), name='customadmin_index'),
   url(r'^unapproved-users$', UnapprovedUsers.as_view(), name='unapproved'),
   url(r'^approve/(?P<user_id>\d+)$', login_required(approve), name='approve'),
)
