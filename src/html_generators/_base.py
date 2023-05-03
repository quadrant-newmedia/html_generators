from html import escape
from typing import Any, Iterable, Iterator

#: type alias; content that is intended to be passed to an HTMLGenerator
#: see generate_child_html to understand how different types will be rendered
Content = Any

class SafeString(str):
	'''
	A str of HTML that plays nicely with other web frameworks.

	These objects will _not_ be escaped when passed to:
	- django templates
	- django.utils.html.conditional_escape
	- markupsafe.escape/markupsafe.Markup.format
	'''
	def __html__(self) -> str:
		return self

class HTMLGenerator:
	'''
	An object representing a balanced chunk of HTML.

	This is the base class for all of our public classes.
	It is not intended to be used directly by end users.
	'''

	def __iter__(self) -> Iterator[str]:
		'''
		Generate a sequence of HTML strings.

		Generally, users will be casting/coercing HTMLGenerators to str, but
		their iterable nature is sometimes useful. For example, you can pass
		them directly to django.http.StreamingHttpResponse().
		'''
		raise NotImplementedError()

	'''
	Note:
	__html__() allows us to be passed directly to markupsafe.Markup, 
	markupsafe.escape, django.utils.html.format_html, and 
	django.utils.html.conditional_escape.

	It does NOT allow us to be printed directly in a django template. django.template.base.Node.render_value_in_context first calls str() 
	on us* (since we're not a subclass of str()), and _then_ calls
	conditional_escape on the result.
	*This is the case in Django 3.1.7, at least. I could see them changing/
	fixing it in the future.
	
	That's why we also have __str__ return a SafeString.
	It _seems_ redundant, but it's not - they cover different scenarios.
	'''
	def __html__(self):
		return str(self)

	def __str__(self) -> SafeString:
		'''
		Convert to a balanced string of HTML.

		Instances are only intended to be converted to a string once.
		Calling this multiple times _may_ produce inconsistent results.

		The returned str is a SafeString, which won't be escaped when passed
		to django templates or markupsafe.
		'''
		return SafeString(''.join(iter(self)))

def generate_child_html(child: Content) -> Iterator[str]:
	'''
	Generate a sequence of HTML strings from the given object.

	The sequence of strings, as a whole, will be a balanced HTML fragment.

	We can't really describe the behaviour of this function any more 
	concisely than the code does, so just read the code.
	'''

	# use case: "conditional children"
	# ie: h.Div(some_test() and 'A conditional child')
	# Do _not_ just check "if child" - h.Div(0) should render <div>0</div>
	if child is None or child is False :
		return

	# Many children will be other (nested) HTMLGenerators
	# Do _not_ call str(child) -> yield directly from it, so that HTML is generated "in order", and we only do string joining at the outer-most level
	if isinstance(child, HTMLGenerator):
		yield from child
		return

	# Support "Safe Strings" from other libraries (ie. Django) that implement __html__ method
	# This allows you to use existing template tag/filter functions without wrapping the output in MarkSafe()
	try :
		html_method = child.__html__
	except (AttributeError, TypeError):
		pass
	else :
		yield html_method()
		return

	# Look for strings _before_ looking for other iterables, since strings are iterable, too
	if isinstance(child, str):
		yield escape(child)
		return
	# If it's iterable, generate html for each of its items
	# Could be a tuple, list, generator expression, etc.
	try :
		i = iter(child)
	except TypeError :
		pass
	else :
		for grandchild in i :
			yield from generate_child_html(grandchild)
		return

	yield escape(str(child))


def generate_html(children: Iterable[Content]) -> Iterator[str]:
	for child in children :
		yield from generate_child_html(child)
