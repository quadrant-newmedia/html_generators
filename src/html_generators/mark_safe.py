from .base import HTMLGenerator

class MarkSafe(HTMLGenerator):
	def __init__(self, string):
		self.string = string

	def __iter__(self):
		yield self.string