from django.conf.urls import patterns, url

from .views import user_login, user_logout
from .views import BeneficiaryRegistrationView, DonorRegistrationView


urlpatterns = patterns('',
   url(r'^register/donor$', DonorRegistrationView.as_view(), name='donor'),
   url(r'^register/beneficiary$',
       BeneficiaryRegistrationView.as_view(), name='beneficiary'),
   url(r'^login/$', user_login, name='login'),
   url(r'^logout/$', user_logout, name='logout'),
)
