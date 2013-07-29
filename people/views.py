from django.views import generic

from people.models import Donor, Beneficiary

class DonorDetailView(generic.DetailView):
    model = Donor
    template_name = 'people/donor_detail.html'
    context_object_name = 'donor'
