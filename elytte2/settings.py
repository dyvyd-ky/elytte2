

STRIPE_API_KEY_PUBLISHABLE = "#"
STRIPE_API_KEY_HIDDEN = "#"

RAZORPAY_API_KEY_PUBLISHABLE = "#"
RAZORPAY_API_KEY_HIDDEN = "#"

PAYPAL_API_KEY_PUBLISHABLE = "#"
PAYPAL_API_KEY_HIDDEN = "#"

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pn)-&b6%y0#j1uad)&%0h-4za-f1ic16@q=#3=(len!7h)++o_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['128.199.222.115', 'sokonisoko.com', 'www.sokonisoko.com']

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'cart'
LOGOUT_REDIRECT_URL = 'frontpage'

# Cart

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

SENDGRID_API_KEY='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'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'elytte'
DEFAULT_EMAIL_FROM = 'elytte.ky@gmail.com'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'apps.cart',
    'apps.coupon',
    'apps.core',
    'apps.newsletter',
    'apps.order',
    'apps.store',
    'apps.userprofile',
    'storages',
    'ckeditor',
    'ckeditor_uploader',
    #'mpesa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elytte2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'elytte2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elyttedb',
        'USER': 'elytte',
        'PASSWORD': 'JmKy1920GG9181995j',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

AWS_ACCESS_KEY_ID = '4OA4PHKRAQH2LQ4KHG7I'
AWS_SECRET_ACCESS_KEY = 'LjbKr8NajlS1LJ7o6XrrAb1tr7mLYrqOMcyaxJcXVw8'

AWS_STORAGE_BUCKET_NAME = 'elytteky'
AWS_S3_ENDPOINT_URL = 'https://elytteky.sgp1.digitaloceanspaces.com'

AWS_S3_CUSTOM_DOMAIN = 'spaces.elytte.com/elytteky'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'elytteky'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
CKEDITOR_UPLOAD_PATH = 'uploads/'

#PESA_ENVIRONMENT = 'sandbox'

#MPESA_CONSUMER_KEY = 'DWqy5Y1qeqjRhu3PGixR1Q7joB8HI0RW'
#MPESA_CONSUMER_SECRET = 'kPY5NZQIgETgAKpU'

#MPESA_SHORTCODE = 'mpesa_shortcode'
#MPESA_EXPRESS_SHORTCODE = 'mpesa_express_shortcode'
#MPESA_SHORTCODE_TYPE = 'till_number'

#MPESA_INITIATOR_USERNAME = 'initiator_username'

#MPESA_INITIATOR_SECURITY_CREDENTIAL = 'initiator_security_credential'