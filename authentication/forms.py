from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(help_text='Enter a valid email address')
	address = forms.CharField()
	website = forms.URLField()
	
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email__iexact=email)
		except User.DoesNotExist:
			return self.cleaned_data['email']
		raise forms.ValidationError(_("Email already exists"))