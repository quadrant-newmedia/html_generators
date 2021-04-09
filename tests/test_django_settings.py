import os

templates_and_static = os.path.join(
    os.path.dirname(__file__), 'test_django_static_and_templates'
)

SECRET_KEY = 'fake'

STATIC_URL = '/static/'
STATICFILES_DIRS = templates_and_static

TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [templates_and_static],
        'APP_DIRS': False,
        'OPTIONS': {
        	'libraries': {
        		'hg_tests': 'tests.test_django_library',
        	}
        }
    },
]

# Makes testing of date filter easier
USE_TZ = False