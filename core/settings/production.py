from core.settings.base import *


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
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
STATICFILES_DIRS = [BASE_DIR / "theme/static/"]
MEDIA_URL = '/media/'
MEDIA_ROOT  =  BASE_DIR / 'media'