import os

SECRET_KEY = '1234'

MIDDLEWARE_CLASSES = tuple()

WITH_WQDB = os.environ.get('WQDB', False)
if WITH_WQDB:
    WQ_APPS = (
        'wq.db.rest',
        'wq.db.rest.auth',
    )
else:
    WQ_APPS = tuple()

WITH_REVERSION = os.environ.get('REVERSION', False)
if WITH_REVERSION:
    REVERSION_APPS = (
        'django.contrib.admin',
        'reversion',
    )
else:
    REVERSION_APPS = tuple()


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'data_wizard',
) + WQ_APPS + REVERSION_APPS + (
    'tests.file_app',
    'tests.data_app',
    'tests.naturalkey_app',
    'tests.eav_app',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data_wizard_test.sqlite3',
    }
}

ROOT_URLCONF = "tests.urls"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

WITH_CELERY = os.environ.get('CELERY', False)

if WITH_CELERY:
    CELERY_RESULT_BACKEND = BROKER_URL = 'redis://localhost/0'

if WITH_WQDB:
    from wq.db.default_settings import *  # noqa

NO_THREADING = os.environ.get('NOTHREADING', False)
if NO_THREADING:
    DATA_WIZARD_BACKEND = 'data_wizard.backends.immediate'
