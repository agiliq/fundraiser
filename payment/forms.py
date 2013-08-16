from django import forms
from django.conf import settings

from .fields import CountryField
from billing import CreditCard

import datetime
# Transaction Modes
MODES = (
    ('TEST', 'TEST'),
    ('LIVE', 'LIVE'),
)

# EBS Payment Form


class PaymentForm(forms.Form):

    account_id = forms.IntegerField(
        initial=settings.EBS_ACCOUNT_ID, required=True)
    reference_no = forms.IntegerField(required=True, initial="223")
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2, required=True, initial='1.00')
    name = forms.CharField(max_length=255, required=True, initial="Sheeba")
    email = forms.EmailField(
        max_length=70, required=True, initial="xyz@ebs.in")
    address = forms.CharField(required=True, initial="Kodambakkam")
    city = forms.CharField(max_length=60, required=True, initial="Chennai")
    state = forms.CharField(max_length=60, required=True, initial="Tamil Nadu")
    country = CountryField()
    postal_code = forms.IntegerField(required=True, initial="600098")
    phone = forms.IntegerField(required=True, initial="044123456")
    # ship_name = forms.CharField(50, label="Shipping Name",initial="Sheeba V")
    # ship_address = forms.CharField(100, label="Shipping Address", initial="Saketh")
    # ship_city = forms.CharField(40, label="Shipping City", initial="New Delhi")
    # ship_state = forms.CharField(40, label="Shipping State", initial="Delhi")
    # ship_country = CountryField(label="Shipping Country")
    # ship_postal_code = forms.CharField(20, label="Shipping Postal Code", initial="110098")
    # ship_phone = forms.CharField(20, label="Shipping Phone", initial="011123456")
    return_url = forms.URLField(
        label="Return URL", required=True, initial=settings.EBS_RETURN_URL + '?DR={DR}')
    description = forms.CharField(required=True, initial="Testing EBS-Django")
    mode = forms.ChoiceField(choices=MODES)

# Stripe payment form

CARD_TYPES = [
    ('', ''),
    ('visa', 'Visa'),
    ('master', 'Master'),
    ('discover', 'Discover'),
    ('american_express', 'American Express'),
    ('diners_club', 'Diners Club'),
    # ('jcb', ''),
    # ('switch', ''),
    # ('solo', ''),
    # ('dankort', ''),
    ('maestro', 'Maestro'),
    # ('forbrugsforeningen', ''),
    # ('laser', 'Laser'),
    ]

today = datetime.date.today()
MONTH_CHOICES = [(m, datetime.date(today.year, m, 1).strftime('%b')) for m in range(1, 13)]
YEAR_CHOICES = [(y, y) for y in range(today.year, today.year + 21)]


class CreditCardForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    number = forms.CharField(required=False)
    card_type = forms.ChoiceField(choices=CARD_TYPES, required=False)
    verification_value = forms.CharField(label='CVV', required=False)

    def clean_year(self):
        year = self.cleaned_data['year']
        if year == str(today):
            raise forms.ValidationError('Year should not be current year')
        return year

    def clean(self):
        data = self.cleaned_data
        credit_card = CreditCard(**data)
        if not credit_card.is_valid():
            raise forms.ValidationError('Credit card validation failed')
        return data


