from django.views import generic

from people.models import Donor, Beneficiary


class DonorDetailView(generic.DetailView):
    model = Donor
    template_name = 'people/donor_detail.html'
    context_object_name = 'donor'


class BeneficiaryDetailView(generic.DetailView):
    model = Beneficiary
    template_name = 'people/beneficiary_detail.html'
    context_object_name = 'beneficiary'
