from pathlib import Path
from django.urls import reverse, reverse_lazy
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

# load environment variables
LOCAL_DEV_ENV_PATH = 'environments/.env_local_dev'

load_dotenv(dotenv_path=LOCAL_DEV_ENV_PATH)
#------------------

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(int(os.getenv('DEBUG', 0)))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'vehicles.apps.VehiclesConfig',
    'service.apps.ServiceConfig',
    'reminders.apps.RemindersConfig',
    'profiles.apps.ProfilesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'my_garage.common.middlewares.save_current_request_middleware',
]

ROOT_URLCONF = 'my_garage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'my_garage.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME', None),
        "USER": os.getenv('DB_USER', None),
        "PASSWORD": os.getenv('DB_PASSWORD', None),
        "HOST": os.getenv('DB_HOST', None),
        "PORT": os.getenv('DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TODO: setup timezone
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Base location in the browser
STATIC_URL = '/static/'

# Location on file system
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

# STATIC_ROOT = os.getenv('STATIC_ROOT')

# Media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = '/media/'

# Login/Logout roots
LOGIN_URL = reverse_lazy('sign in')
LOGIN_REDIRECT_URL = reverse_lazy('garage')
LOGOUT_REDIRECT_URL = reverse_lazy('sign in')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Initialising the user model
AUTH_USER_MODEL = 'profiles.AppUser'

CACHES = {
    'default': {
        'BACKEND':
            'django.core.cache.backends.redis.RedisCache',
            'LOCATION': os.getenv('CACHE_REDIS_DB_LOCATION'),
            "NAME": os.getenv('CACHE_REDIS_DB_NAME'),
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         "LOCATION": "app_cache",
#     }
# }

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', None)
EMAIL_PORT = os.getenv('EMAIL_PORT', None)
EMAIL_USE_TLS = bool(int(os.getenv('EMAIL_USE_TLS', 0)))   
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
