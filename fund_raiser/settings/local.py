from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'django_extensions',
)

"""
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = "shiva@agiliq.com"

# MERCHANT SETTINGS
MERCHANT_TEST_MODE = True
MERCHANT_SETTINGS = {
    # Stripe Payment Settings
    "stripe": {
        "API_KEY": get_env_variable('MERCHANT_API_KEY'),
        "PUBLISHABLE_KEY": get_env_variable('MERCHANT_PUBLISHABLE_KEY'),
    }
}

"""


# Configs for EBS Payment
# Enter Your Account Id here.This is a test id.
EBS_ACCOUNT_ID = get_env_variable('EBS_ACCOUNT_ID')

# Enter Your Secret Key here.This is a test key.
EBS_SECRET_KEY = get_env_variable('EBS_SECRET_KEY')

# Do not edit this URL.
EBS_ACTION_URL = 'https://secure.ebs.in/pg/ma/sale/pay'

# Enter your domain URL instead of 127.0.0.1:8000.
EBS_RETURN_URL = 'http://127.0.0.1:8000/ebs/ebspayment/response'

# Gmail Import Contacts
GOOGLE_COOKIE_CONSENT = 'google_token_consent'  # This string can be anything
# This string can be anything
GOOGLE_REDIRECT_SESSION_VAR = 'google_contacts_redirect'
GOOGLE_REDIRECT_BASE_URL = 'http://localhost:8000'

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# Admin Email Settings
EMAIL_SUBJECT_PREFIX = 'Pratham Books : '
