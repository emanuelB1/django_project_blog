from .base import *
from django.core.files.storage import FileSystemStorage

""""
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
""""
STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles/')

MEDIA_ROOT = Path.joinpath(BASE_DIR, 'mediafiles/')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'