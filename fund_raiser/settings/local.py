from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DB_NAME = get_env_variable('DB_NAME')
DB_USER = get_env_variable('DB_USER')
DB_PASSWORD = get_env_variable('DB_PASSWORD')

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

EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = "shiva@agiliq.com"

# MERCHANT SETTINGS
MERCHANT_TEST_MODE = True
MERCHANT_SETTINGS = {
    # Stripe Payment Settings
    "stripe": {
        "API_KEY" : 'sk_test_4JHUaTtmtU8cnYoS8uEzQnRZ',
        "PUBLISHABLE_KEY" : 'pk_test_k0vg9IfB2dYLbnZCa2EnR24H'
    }
}
