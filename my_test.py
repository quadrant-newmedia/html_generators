#!/usr/bin/env python
from django.conf import settings
settings.configure(
	DATABASES=[],
	ROOT_URLCONF='test_urls.py',
	INSTALLED_APPS=[],
)
import django
django.setup()




from django.urls import reverse
reverse('a')

print('Hooray!')