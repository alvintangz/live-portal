import os
import portal.variables as imp

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#_6j@i@j*=sb6y5+6g25@x@su8)-ju*q9@32i=@z&9!^6t9whz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
	'users.apps.UsersConfig',
    'notifications.apps.NotificationsConfig',
    'rounds.apps.RoundsConfig',
    'corporate.apps.CorporateConfig',
    'contacts.apps.ContactsConfig',
    'qanda.apps.QandaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

if not DEBUG:
	INSTALLED_APPS += ['storages',]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'portal/templates/')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if DEBUG:
	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.sqlite3',
        	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    	}
	}
else:
	DATABASES = {
    	'default': {
        	'ENGINE': 'sql_server.pyodbc',
        	'NAME': os.environ.get('LP_DB_NAME', ''),
        	'USER': os.environ.get('LP_DB_USER', ''),
        	'PASSWORD': os.environ.get('LP_DB_PASSWORD', ''),
        	'HOST': os.environ.get('LP_DB_HOST', ''),
        	'PORT': os.environ.get('LP_DB_PORT', ''),
        	'OPTIONS': {
            	'driver': 'ODBC Driver 13 for SQL Server',
        	},
    	},
	}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ['portal/static/']

if not DEBUG:
	DEFAULT_FILE_STORAGE = 'portal.custom_azure.AzureMediaStorage'
	STATICFILES_STORAGE = 'portal.custom_azure.AzureStaticStorage'
	STATIC_LOCATION = "static"
	MEDIA_LOCATION = "media"
	AZURE_ACCOUNT_NAME = "liveportal2019"
	AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
	STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
	MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

# User authentication
LOGIN_URL = 'sign-in'
LOGIN_REDIRECT_URL = 'index'
AUTH_USER_MODEL = 'users.User'

# Sessions time limit
SESSION_COOKIE_AGE = 86400

# Media - Files uploaded by user
MEDIA_URL = "/media/"
MEDIA_ROOT = "media/"

# Email
EMAIL_BACKEND = imp.email["backend"]
EMAIL_HOST = imp.email["host"]
EMAIL_PORT = imp.email["port"]
EMAIL_HOST_USER = imp.email["user"]
EMAIL_HOST_PASSWORD = imp.email["password"]
EMAIL_USE_TLS = imp.email["tls"]
DEFAULT_FROM_EMAIL = imp.email["from"]

# Other production settings
if not DEBUG:
	ADMINS = [('Alvin', 'alvin.tang@mail.utoronto.ca'),]
	CSRF_COOKIE_SECURE = False
	SESSION_COOKIE_SECURE = False