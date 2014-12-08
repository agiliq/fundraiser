from django.conf.urls import patterns, url
from django.views.generic import ListView

from people.models import Person
from people.views import PersonDetailView


urlpatterns = patterns('',
                       url(r'^persons/$',
                           ListView.as_view(template_name='people/person.html',
                                            queryset=Person.objects.all(),
                                            context_object_name='person_list',
                                            paginate_by=10), name='list'),
                       url(r'^person/detail/(?P<pk>\d+)/$',
                           PersonDetailView.as_view(),
                           name='person_detail'), )
