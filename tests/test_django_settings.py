SECRET_KEY = 'fake'

TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['tests'],
        'APP_DIRS': False,
        'OPTIONS': {
        	'libraries': {
        		'hg_tests': 'tests.test_django_library',
        	}
        }
    },
]