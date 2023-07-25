import os
from pathlib import Path

from dotenv import load_dotenv

from djblogger.logging import *
from djblogger.settings.base import *

load_dotenv(Path.joinpath(BASE_DIR, '.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

ROOT_URLCONF = 'djblogger.urls'


STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles/')



STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'