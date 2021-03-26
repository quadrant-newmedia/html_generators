from .base import HTMLGenerator, generate_html

class Document(HTMLGenerator):
	'''
		A complete HTML document

		Merely adds the required DOCTYPE line.
	'''
	def __init__(self, *children):
		self._children = children

	def __iter__(self):
		yield '<!DOCTYPE html>\n'
		yield from generate_html(self._children)