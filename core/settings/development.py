from core.settings.base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}



DEBUG = True
STATICFILES_DIRS = ["theme/static/"]
MEDIA_URL = '/media/'
MEDIA_ROOT  =  'media'