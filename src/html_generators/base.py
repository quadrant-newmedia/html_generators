from html import escape

class SafeString(str):
	'''
		This object can be used anywhere a string can be used. 
		
		Further, since it implements __html__(self), many frameworks (like Django) know that it doesn't need further escaping.
	'''
	def __html__(self):
		return self

class HTMLGenerator:
	def __str__(self):
		return SafeString(''.join(iter(self)))

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
