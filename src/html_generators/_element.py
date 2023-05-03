from . import _utils as utils
from ._base import Content, HTMLGenerator, escape, generate_html, SafeString
from ._mark_safe import MarkSafe

def open_tag(name, attrs):
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

def normalize(attr):
	'''
	Convert a keyword parameter name to an HTML attribute name.

	Trailing underscores are trimmed. This allows you to pass "class_" as a 
	keyword argument, and we'll convert to "class" (which is a reserved word
	in python, so you can't use it as a keyword argument).

	Other underscores are replaced with hyphens. Hyphens are often used in 
	attribute names (data-* attributes, and custom attributes).

	Note - this algorithm does NOT allow you to encode any possible HTML 
	attribute name as a python keyword argument, but it covers every
	attribute I've ever seen in actual use.
	'''
	return attr.rstrip('_').replace('_', '-')
def normalize_dict(attrs):
	return {normalize(attr): value for attr, value in attrs.items()}

class Element(HTMLGenerator):
	'''
	A "normal" HTML Element 

	https://html.spec.whatwg.org/multipage/syntax.html#elements-2

	name_: the element name
	- Note - the trailing underscore is so we don't collide with html name attribute

	*children:
	- these are the child nodes (text and elements) of this element

	**attrs:
	- the HTML attributes of this element
	'''
	# TODO - document that attrs are OPTIONAL strings
	def __init__(self, name_, *children: Content, **attrs: str):
		self._name = name_
		self._children = children
		self._attrs = normalize_dict(attrs)

	def __iter__(self):
		yield from open_tag(self._name, self._attrs)
		yield from generate_html(self._children)
		yield f'</{self._name}>'

	def open_tag(self):
		'''
		Generate just the open tag, as a MarkSafe instance.
		Useful when translating strings via h.format()
		'''
		return MarkSafe(''.join(open_tag(self._name, self._attrs)))
	def close_tag(self):
		'''
		Generate just the close tag, as a MarkSafe instance.
		Useful when translating strings via h.format()
		'''
		return MarkSafe(f'</{self._name}>')

	def with_attrs(self, **attrs):
		'''
		Clone the element, with additional attributes.

		Attribute names are normalized just like in __init__.
		You can remove an existing attribute by setting it to None.
		'''
		clone = self.__class__(self._name)
		clone._children = list(self._children)
		clone._attrs = dict(self._attrs, **normalize_dict(attrs))
		return clone
	def with_classes(self, *classes):
		'''Clone the element, with additional classes.'''
		return self.with_attrs(
			class_=utils.classes(self._attrs.get('class'), *classes),
		)
	def with_styles(self, *styles):
		'''Clone the element, with additional styles.'''
		return self.with_attrs(
			style=utils.styles(self._attrs.get('style'), *styles),
		)

class VoidElement(Element):
	'''
	A Void HTML Element 

	See https://html.spec.whatwg.org/multipage/syntax.html#elements-2)

	Works just like Element, but doesn't allow you to pass any children.

	Note - name_ is so that h.VoidElement('input', name='FOO') doesn't complain about multiple values for argument 'name'
	Ideally, we'd use (self, name, /, **attrs) to specify that name is positional-only, but that's only available in 3.9
	'''
	def __init__(self, name_, **attrs):
		super().__init__(name_, **attrs)

	def __iter__(self):
		yield from open_tag(self._name, self._attrs)

	def close_tag(self):
		return ''

class RawTextElement(Element):
	'''
	A Raw Text HTML Element (script/style)

	We do NOT escape the content of these elements, because html entities 
	inside them are not parsed by browsers.

	It's up to the user to ensure that the content passed to these elements
	is "safe" - it must not contain anything that "matches the closing tag"
	of that element.
	
	https://html.spec.whatwg.org/multipage/syntax.html#elements-2
	https://html.spec.whatwg.org/multipage/syntax.html#cdata-rcdata-restrictions)
	'''
	def __init__(self, name, *content, **attrs):
		super().__init__(name, **attrs)
		self._content = content

	def __iter__(self):
		yield from open_tag(self._name, self._attrs)
		
		# stringify whatever the user passed in.
		# It's our responsibility to only generate str instances (otherwise it can lead to hard-to-debug errors).
		# It's probably faster to do this than to "assert isinstance(content, str)", and the user might expect us to support "stringifiable" things, anway -- ie: h.Script(h.Div('This is a template'), type='text/template')
		yield from (str(c) for c in self._content)

		yield f'</{self._name}>'
