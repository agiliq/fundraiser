from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth import logout, login, authenticate
from django.template import RequestContext

from authentication.forms import LoginForm
from books.models import Book
from people.forms import BeneficiaryForm, DonorForm
from people.models import Beneficiary, Donor


def register(request):
    formname = None
    if request.path == reverse('accounts:beneficiary'):
        form = BeneficiaryForm()
        if request.method == 'POST':
            form = BeneficiaryForm(request.POST)
            formname = 'Beneficiary'
            if form.is_valid():
                new_user = User.objects.create_user(username=form.cleaned_data[
                                                    'ben_name'], password=form.cleaned_data['password1'])
                new_user.profile.is_beneficiary = True
                new_user.profile.save()
                beneficiary = Beneficiary.objects.create(
                    user=new_user, address=form.cleaned_data['address'],
                                              website=form.cleaned_data['website'])
                user = authenticate(username=form.cleaned_data[
                                    'ben_name'], password=form.cleaned_data['password1'])
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
                                                    'donor_name'], password=form.cleaned_data['password1'])
                new_user.profile.is_donor = True
                new_user.profile.save()
                donor = Donor.objects.create(user=new_user,
                                            address=form.cleaned_data[
                                                'address'],
                                            website=form.cleaned_data[
                                                'website'],
                                          )
                user = authenticate(username=form.cleaned_data[
                                    'donor_name'], password=form.cleaned_data['password1'])
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
                error_login = "Your username or password is incorrect."
    return render_to_response("authentication/login.html", {'form': login_form, 'errors': dict(login_form.errors.viewitems()),'error_login':error_login},
                              context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def customadmin_index(request):
    books = Book.objects.all()
    return render_to_response('authentication/customadmin_index.html', {"books": books}, context_instance=RequestContext(request))


def approve(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.beneficiary.is_approved = True
        user.beneficiary.save()
        return HttpResponseRedirect(reverse('customadmin:unapproved'))
    return render_to_response('unapproved_users.html')


class UnapprovedUsers(ListView):
    template_name = 'authentication/unapproved_users.html'
    context_object_name = 'unapproved_users'

    def get_queryset(self):
        """
        Returns the unapproved users related to beneficiary in
        the database

        """

        return User.objects.filter(beneficiary__is_approved=False)
