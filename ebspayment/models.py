# Create your models here.
from django import forms
from ebspayment.fields import CountryField
from django.conf import settings

#Transaction Modes
MODES = (
     ('TEST', 'TEST'),
     ('LIVE', 'LIVE'),
)

#EBS Payment Form
class PaymentForm(forms.Form):
   
    account_id = forms.IntegerField(initial=settings.EBS_ACCOUNT_ID, required=True)
    reference_no = forms.IntegerField(required=True, initial="223")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True, initial='1.00')
    name = forms.CharField(max_length=255, required=True, initial="Sheeba") 
    email = forms.EmailField(max_length=70, required=True, initial="xyz@ebs.in")
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
    return_url = forms.URLField(label="Return URL", required=True, initial=settings.EBS_RETURN_URL+'?DR={DR}')
    description = forms.CharField(required=True, initial="Testing EBS-Django")
    mode = forms.ChoiceField(choices=MODES)
