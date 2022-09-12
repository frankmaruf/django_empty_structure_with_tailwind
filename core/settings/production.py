from core.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DataBaseName',
        'USER': 'DataBaseUserName',
        'PASSWORD': 'DataBasePASSWORD',
        'HOST': '127.0.0.1',
        'NAME': '5432',
    }
}

DEBUG = False
STATICFILES_DIRS = ["theme/static/"]
MEDIA_URL = '/media/'
MEDIA_ROOT  =  'media'