from html import escape

class HTMLGenerator:
	def __str__(self):
		return ''.join(self)

def yield_child(child):
	if not child :
		return
	if isinstance(child, HTMLGenerator):
		yield from child
		return
	if isinstance(child, str):
		yield escape(child)
		return
	try :
		i = iter(child)
	except TypeError :
		'''
			Its neither string, iterable, nor HTMLGenerator
			Cast to string and escape it.
		'''
		yield escape(str(child))
	else :
		for grandchild in i :
			yield from yield_child(grandchild)

def yield_children(children):
	for child in children :
		yield from yield_child(child)