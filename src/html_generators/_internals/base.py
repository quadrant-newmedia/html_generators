from html import escape
from typing import Any, Iterable, Iterator

class SafeString(str):
	'''
		A str of HTML that plays nicely with other web frameworks.

		These objects will _not_ be escaped when passed to:
		- django.utils.html.conditional_escape
		- markupsafe.escape
	'''
	def __html__(self):
		return self

class HTMLGenerator:
	'''
		An object representing a balanced chunk of HTML.

		This is the base class for all of our public classes.
		It is not intended to be used directly by end users.
	'''
	def __str__(self):
		return SafeString(''.join(iter(self)))

def generate_child_html(child: Any) -> Iterator[str]:
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


def generate_html(children: Iterable[Any]) -> Iterator[str]:
	for child in children :
		yield from generate_child_html(child)
