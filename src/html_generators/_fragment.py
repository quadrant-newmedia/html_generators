from ._base import HTMLGenerator, generate_html

class Fragment(HTMLGenerator):
	'''
		A (balanced) fragment of one or more html nodes.

		Note that you generally won't need to use this class, since you can pass any iterable directly to Document, Element, etc. 

		Useful only when you need to render multiple nodes directly to a string (ie. to pass off to some other template system, or to generate the body of an HTML email).
	'''
	def __init__(self, *children):
		self._children = children

	def __iter__(self):
		yield from generate_html(self._children)