from ._base import Content, HTMLGenerator, generate_child_html
from typing import Iterable, Iterator

class Join(HTMLGenerator):
	'''
	Similar to str.join
	
	The "joiner" and the "items" need not be strings (they can be other HTMLGenerators, numbers, etc.).

	"items" MAY contain "empty values" (None, False) - 
	they will NOT cause an extra joiner to be rendered.
	'''
	def __init__(self, joiner: Content, items: Iterable[Content]):
		# Stringify joiner only once.
		self._joiner = str(joiner)
		self._items = items

	def __iter__(self):
		first_item = True
		for child in self._items :
			# Skip "explicitly empty" items, just like all other generators
			# Be sure we do NOT add a joiner for this empty item
			if child is None or child is False :
				continue

			if not first_item :
				yield self._joiner
			else :
				first_item = False

			# child could be another HTMLGenerator, iterable, etc.
			yield from generate_child_html(child)