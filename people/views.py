from django.views import generic

from people.models import Person


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'people/person_detail.html'
    context_object_name = 'person'
