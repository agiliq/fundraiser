from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fundraiser.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')

# MERCHANT SETTINGS
MERCHANT_TEST_MODE = True
MERCHANT_SETTINGS = {
    # Stripe Payment Settings
    "stripe": {
        "API_KEY": get_env_variable('MERCHANT_API_KEY'),
        "PUBLISHABLE_KEY": get_env_variable('MERCHANT_PUBLISHABLE_KEY'),
    }
}


# Configs for EBS Payment
# Enter Your Account Id here.This is a test id.
EBS_ACCOUNT_ID = get_env_variable('EBS_ACCOUNT_ID')

# Enter Your Secret Key here.This is a test key.
EBS_SECRET_KEY = get_env_variable('EBS_SECRET_KEY')