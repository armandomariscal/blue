from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR + '/static/',
)

MEDIA_ROOT = (
        BASE_DIR + '/media/'
)

MEDIA_URL = '/media/'

DEBUG = True
PRODUCCION = True
USE_TZ = True
USE_I18N = True

LOGIN_URL = '/signin/'
