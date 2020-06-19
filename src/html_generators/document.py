from .base import HTMLGenerator, yield_children

class Document(HTMLGenerator):
	def __init__(self, *children):
		self.children = children

	def __iter__(self):
		yield '<!DOCTYPE html>\n'
		yield from yield_children(self.children)