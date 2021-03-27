from ._base import HTMLGenerator

class Comment(HTMLGenerator):
	'''
		An HTML comment node

		It's up to the user to ensure that content does not contain '-->'.
		
		Not really sure why you'd need to add comments (your code can just have python comments), but it's here in case you need it.
	'''
	def __init__(self, content):
		self._content = content

	def __iter__(self):
		yield '<!--'
		yield str(self._content)
		yield '-->'