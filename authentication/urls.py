from django.conf.urls import patterns, url
from authentication.views import register, user_login, user_logout
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       url(r'^register/donor$', register, name='donor'),
                       url(r'^register/beneficiary$',
                           register, name='beneficiary'),
                       url(r'^register/registration_completed$', TemplateView.as_view(
                           template_name="authentication/registration_completed.html"), name='reg_cmpltd'),
                       url(r'^login/$', user_login, name='login'),
                       url(r'^logout/$', user_logout, name='logout'),

                       )
