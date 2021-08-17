from ._base import HTMLGenerator, generate_html
from ._standard_elements import Html

class Document(HTMLGenerator):
	'''
		A complete HTML document

		Merely adds the required DOCTYPE line.

		If you specify html_attrs, all children will be wrapped in an <html>
		element with the specified attrs. Just a shortcut.
	'''
	def __init__(self, *children, **html_attrs):
		self._children = [Html(children, **html_attrs)] if html_attrs else children

	def __iter__(self):
		yield '<!DOCTYPE html>\n'
		yield from generate_html(self._children)