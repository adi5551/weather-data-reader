import os

from weather_data_reader.settings import *  # noqa
from weather_data_reader.settings import BASE_DIR  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_database.db'),
    },
}