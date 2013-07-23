from django import forms as newform
from django.forms import ModelForm
from books.models import Beneficiary, Donor
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# from django.core.urlresolvers import reverse
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Fieldset

class LoginForm(newform.Form):
    username = newform.CharField()
    password = newform.CharField(widget=newform.PasswordInput)

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'login-form'
    #     self.helper.form_class = 'form-horizontal'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = reverse('accounts:login')
    #     self.helper.add_input(Submit('submit', 'Login', css_class='btn btn-primary'))


class BeneficiaryForm(ModelForm):

    class Meta:
        model = Beneficiary
        exclude = ('beneficiary_user', 'approved',)

    password1 = newform.CharField(
        widget=newform.PasswordInput(), label=(u'password'))
    password2 = newform.CharField(
        widget=newform.PasswordInput(), label=(u'password (again)'))

    def clean_beneficiary_name(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['beneficiary_name'])
        except Exception as e:
            return self.cleaned_data['beneficiary_name']
        raise newform.ValidationError(_(
            "This username is already taken. Please choose another."))

    def clean_password2(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise newform.ValidationError(_(
                    u'You must type the same password each time'))
        return self.cleaned_data


class DonorForm(ModelForm):

    class Meta:
        model = Donor
        exclude = ('donor_user',)

    donor_name = newform.CharField(max_length=100)
    password1 = newform.CharField(
        widget=newform.PasswordInput(), label=(u'password'))
    password2 = newform.CharField(
        widget=newform.PasswordInput(), label=(u'password (again)'))


    def clean_donor_name(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['donor_name'])
        except Exception as e:
            return self.cleaned_data['donor_name']
        raise newform.ValidationError(_(
            "This username is already taken. Please choose another."))

    def clean_password2(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise newform.ValidationError(_(
                    u'You must type the same password each time'))
        return self.cleaned_data
