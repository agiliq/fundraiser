from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.template import RequestContext
from authentication.forms import BeneficiaryForm, DonorForm
from books.models import Beneficiary, Donor


def register(request):
    form = BeneficiaryForm()
    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data[
                                                'beneficiary_name'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            beneficiary = Beneficiary.objects.create(beneficiary_user=new_user, beneficiary_name=form.cleaned_data['beneficiary_name'],
            	                      email=form.cleaned_data['email'], ben_type=form.cleaned_data['ben_type'],
            	                      strength=form.cleaned_data['strength'], address=form.cleaned_data['address'],
            	                      city=form.cleaned_data['city'], state=form.cleaned_data['state'],
            	                      country=form.cleaned_data['country'], phone=form.cleaned_data['phone'],
            	                      fax=form.cleaned_data['fax'],website=form.cleaned_data['website'] )



    return render_to_response('authentication/registration.html', {'form': form,'errors':dict(form.errors.viewitems())}, context_instance=RequestContext(request))
