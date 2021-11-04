'''
html_generators.django

Utilities for using html_generators within a django project.
This is the only module within html_generators that has any django 
dependencies.

As well as providing some new/wrapper functionality, we also provide 
convenient aliases for some of django's built-in template tags/filters.

Some of the contents of this module have names that clash with
standard python classes/functions, so we intend you to import 
this entire module with a convenient alias:
import html_generators.django as hd
'''
from ._base import HTMLGenerator
import datetime
from django.conf import settings
from django.templatetags.static import static
from django.template.defaultfilters import date as _date
from django.template.loader import render_to_string
from django.utils.timezone import is_naive, get_current_timezone

__all__ = [
	'date', 'static', 'Template',
]

DEFAULT = object()

def date(value, format=None, use_tz=None):
	'''
	Works similar to the django date templatefilter.

	Note that we delegate to django's own filter function, but that function 
	does NOT handle timezone conversions - that's handled separately by the 
	template layer. So we have to do it ourselves.
	'''
	if (
		isinstance(value, datetime.datetime) and
		(settings.USE_TZ if use_tz is None else use_tz) and
		not is_naive(value)
	) :
		value = value.astimezone(get_current_timezone())

	return _date(value, format)

class Template(HTMLGenerator):
	'''
	Renders a django template with given request/context.

	You could just call render_to_string in your own code, but then:
		- you'd have to wrap it in html_generators.MarkSafe
		- string generation would be done "out of order"

	That second issue is mostly just academic, but it could have some slight 
	performance ramifications if you were generating a large streaming 
	response. With html_generators, we're trying to be consistent about 
	rendering all content "just in time", and this utility 
	helps achieve that.
	'''
	def __init__(self, template_name, request=None, context=None, using=None):
		self.template_name = template_name
		self.request = request
		self.context = context
		self.using = using

	def __iter__(self):
		yield render_to_string(
			self.template_name, 
			context=self.context, 
			request=self.request, 
			using=self.using
		)

# backward compatible alias
DjangoTemplate = Template
