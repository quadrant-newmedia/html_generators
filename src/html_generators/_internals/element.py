from .base import HTMLGenerator, escape, generate_html
from .utils import classes, styles

def _open_tag(name, attrs):
	yield '<'+name
	for key, value in attrs.items() :
		if value is False or value is None :
			continue
		yield ' '
		yield key
		if value is True :
			continue
		yield f'="{escape(str(value))}"'
	yield '>'

def _normalize(attr):
	'''
		strip('_')
			this allows you to postfix attribute names with an underscore when those names clash with python keywords (as recommended in PEP 8 - https://www.python.org/dev/peps/pep-0008/#id46)

			Note- we use strip, rather than rstrip, for backward compatibility (we used to recommend prefixing with an _, but now recommend postfix, to align with PEP 8)

		replace('_', '-')
			'-' is important in attribute names (for data-* attributes and custom attributes), '_' is not. You can write python keyword argument names with '_' and they will converted to '-'

			Technically, '_' characters are allowed in custom attribute names (I think), but I've never seen them used. We do not currently support them.
	'''
	return attr.strip('_').replace('_', '-')
def _normalize_dict(attrs):
	return {_normalize(attr): value for attr, value in attrs.items()}

class Element(HTMLGenerator):
	'''
		A "normal" HTML Element 

		See https://html.spec.whatwg.org/multipage/syntax.html#elements-2
	'''
	def __init__(self, name, *children, **attrs):
		self._name = name

		'''
			Note - we haven't written documentation for this package yet, but we should officially document these, and endorse their mutation (after initialization, before rendering).

			This is especially helpful if you want to create "wrapper elements" which mutate their children.
		'''
		self._children = children

		'''
			Note we normalize attrs at initialization, rather than at rendering time.
			This makes methods like add_classes simpler.
		'''
		self._attrs = _normalize_dict(attrs)

	def with_attrs(self, **attrs):
		clone = self.__class__(self._name)
		clone._children = list(self._children)
		clone._attrs = dict(self._attrs, **_normalize_dict(attrs))
		return clone
	def with_classes(self, *_classes):
		return self.with_attrs(class_=classes(self._attrs.get('class'), *_classes))
	def with_styles(self, *_styles):
		return self.with_attrs(style=styles(self._attrs.get('style'), *_styles))

	def __iter__(self):
		yield from _open_tag(self._name, self._attrs)
		yield from generate_html(self._children)
		yield f'</{self._name}>'

class VoidElement(Element):
	'''
		A Void HTML Element (see https://html.spec.whatwg.org/multipage/syntax.html#elements-2)
	'''
	def __init__(self, name, **attrs):
		super().__init__(name, **attrs)

	def __iter__(self):
		yield from _open_tag(self._name, self._attrs)

class RawTextElement(Element):
	'''
		A Raw Text HTML Element (script/style)

		See https://html.spec.whatwg.org/multipage/syntax.html#elements-2

		We do NOT escape the content of these elements, because html entities inside them are not parsed by browsers.
		It's up to the user to ensure that the content passed to these elements is "safe" - it must not contain anything that "matches the closing tag" of that element.
		See https://html.spec.whatwg.org/multipage/syntax.html#cdata-rcdata-restrictions)

		Note about IGNORE	
	'''
	def __init__(self, name, content='', *IGNORE, **attrs):
		super().__init__(name, **attrs)
		self.content = content

	def __iter__(self):
		yield from _open_tag(self._name, self._attrs)
		
		# stringify whatever the user passed in.
		# It's our responsibility to only generate str instances (otherwise it can lead to hard-to-debug errors).
		# It's probably faster to do this than to "assert isinstance(content, str)", and the user might expect us to support "stringifiable" things, anway -- ie: h.Script(h.Div('This is a template'), type='text/template')
		yield str(self.content)

		yield f'</{self._name}>'
