from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.template import RequestContext
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm
from people.models import Beneficiary, Donor
from profiles.tasks import sendemail


class RegistrationView(FormView):

    template_name = "authentication/registration.html"
    form_class = RegistrationForm
    person_klass = None

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.save()
        self.person_klass_specific_stuff(form, user)
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
        if user is not None and user.is_active:
            login(self.request, user)
            sendemail.delay(
                sub="reg_sub", msg="reg_msg", to=user.email, user=user)
        return super(RegistrationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('books:listofbooks')


class DonorRegistrationView(RegistrationView):

    person_klass = Donor

    def get_context_data(self, **kwargs):
        kwargs = super(DonorRegistrationView, self).get_context_data(**kwargs)
        kwargs['formname'] = 'Donor'
        kwargs['post_url'] = reverse('accounts:donor')
        return kwargs

    def person_klass_specific_stuff(self, form, user):
        user.profile.is_donor = True
        user.profile.save()
        self.person_klass.objects.create(
            user=user, address=form.cleaned_data['address'],
            website=form.cleaned_data['website'])


class BeneficiaryRegistrationView(RegistrationView):

    person_klass = Beneficiary

    def get_context_data(self, **kwargs):
        kwargs = super(BeneficiaryRegistrationView, self).get_context_data(
            **kwargs)
        kwargs['formname'] = 'Beneficiary'
        kwargs['post_url'] = reverse('accounts:beneficiary')
        return kwargs

    def person_klass_specific_stuff(self, form, user):
        user.profile.is_beneficiary = True
        user.profile.save()
        self.person_klass.objects.create(
            user=user, address=form.cleaned_data['address'],
            website=form.cleaned_data['website'])


def user_login(request):
    next = None
    if request.GET:
        next = request.GET['next']
    login_form = AuthenticationForm()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('books:listofbooks'))
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            if next == None:
                return HttpResponseRedirect(reverse('books:listofbooks'))
            else:
                return HttpResponseRedirect(next)
    return render_to_response("authentication/login.html",
                {'form': login_form, 'next': next}, context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
