from .common import *

SECRET_KEY = 'django-insecure-z@h7#*125n^^45^baqkab%2^*!losr#o+o4vlbk4gz47fo%ro!'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
