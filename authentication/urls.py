from django.conf.urls import patterns, url

from authentication.views import user_login, user_logout
from authentication.views import customadmin_index, approve, UnapprovedUsers
from authentication.views import BeneficiaryRegistrationView, DonorRegistrationView


urlpatterns = patterns('',
   url(r'^register/donor$', DonorRegistrationView.as_view(), name='donor'),
   url(r'^register/beneficiary$',
       BeneficiaryRegistrationView.as_view(), name='beneficiary'),
   url(r'^login/$', user_login, name='login'),
   url(r'^logout/$', user_logout, name='logout'),

   url(r'^$', customadmin_index, name='customadmin_index'),
   url(r'^unapproved-users$', UnapprovedUsers.as_view(), name='unapproved'),
   url(r'^approve/(?P<user_id>\d+)$', approve, name='approve'),

)
