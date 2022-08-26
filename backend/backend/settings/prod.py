import os
from .common import *

SECRET_KEY = "GOFUCKYOURSELF"

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost","161.35.110.5","www.sundaysbackenddomainname.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sundays',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Ac3ZY!4yMJNKdqH'
    }
}
