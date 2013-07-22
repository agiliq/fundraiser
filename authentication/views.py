from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.template import RequestContext
from authentication.forms import BeneficiaryForm, DonorForm, LoginForm
from books.models import Beneficiary, Donor


def register(request):
    formname=None
    if request.path == reverse('accounts:beneficiary'):
        form = BeneficiaryForm()
        if request.method == 'POST':
            form = BeneficiaryForm(request.POST)
            formname = 'Beneficiary'
            if form.is_valid():
                new_user = User.objects.create_user(username=form.cleaned_data[
                                                    'beneficiary_name'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
                new_user.profile.is_beneficiary = True
                new_user.profile.save()
                beneficiary = Beneficiary.objects.create(
                    beneficiary_user=new_user, beneficiary_name=form.cleaned_data[
                        'beneficiary_name'],
                                              email=form.cleaned_data[
                                                  'email'], ben_type=form.cleaned_data['ben_type'],
                                              strength=form.cleaned_data[
                                                  'strength'], address=form.cleaned_data['address'],
                                              city=form.cleaned_data[
                                                  'city'], state=form.cleaned_data['state'],
                                              country=form.cleaned_data[
                                                  'country'], phone=form.cleaned_data['phone'],
                                              fax=form.cleaned_data['fax'], website=form.cleaned_data['website'])
                user = authenticate(username=form.cleaned_data['beneficiary_name'], password=form.cleaned_data['password1'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('books:listofbooks'))

                return HttpResponseRedirect(reverse('books:listofbooks'))
    else:
        form = DonorForm()
        if request.method == 'POST':
            form = DonorForm(request.POST)
            formname = 'Donor'
            if form.is_valid():
                new_user = User.objects.create_user(username=form.cleaned_data[
                                                    'donor_name'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
                new_user.profile.is_donor = True
                new_user.profile.save()
                donor = Donor.objects.create(
                    donor_user=new_user, 
                                          email=form.cleaned_data[
                                              'email'], address=form.cleaned_data['address'],
                                          city=form.cleaned_data[
                                              'city'], state=form.cleaned_data['state'],
                                          country=form.cleaned_data[
                                              'country'], phone=form.cleaned_data['phone'],
                                          fax=form.cleaned_data['fax'], website=form.cleaned_data['website'],
                                          )
                user = authenticate(username=form.cleaned_data['donor_name'], password=form.cleaned_data['password1'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('books:listofbooks'))

    return render_to_response('authentication/registration.html', {'form': form,'formname':formname, 'errors':dict(form.errors.viewitems())}, context_instance=RequestContext(request))


def user_login(request):
    error_login = None
    login_form = LoginForm()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('books:listofbooks'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('books:listofbooks'))
                else:
                    error_login = "Your account is not active, please contact the site admin."
            else:
                error_login = "Your username or password is incorrect."
    return render_to_response("authentication/login.html", {'form': login_form, 'errors': dict(login_form.errors.viewitems()),'error_login':error_login},
                              context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
