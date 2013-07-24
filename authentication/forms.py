from django import forms as newform
from django.forms import ModelForm
from people.models import Beneficiary, Donor
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
    # self.helper.add_input(Submit('submit', 'Login', css_class='btn btn-
    # primary'))
