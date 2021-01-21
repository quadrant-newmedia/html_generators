from .base import HTMLGenerator, escape, yield_children
from .utils import classes, styles
from functools import partial

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

class Element(HTMLGenerator):
	'''
		A Normal HTML Element (see https://html.spec.whatwg.org/multipage/syntax.html#elements-2)
	'''
	def __init__(self, _name, *_children, **attrs):
		self.name = _name

		'''
			Note - we haven't written documentation for this package yet, but we should officially document these, and endorse their mutation (after initialization, before rendering).

			This is especially helpful if you want to create "wrapper elements" which mutate their children.
		'''
		self.children = _children

		'''
			Note we normalize attrs at initialization, rather than at rendering time.
			This makes methods like add_classes simpler.
		'''
		self.attrs = {_normalize(attr): value for attr, value in attrs.items()}

	def add_classes(self, *_classes):
		self.attrs['class'] = classes(self.attrs.get('class'), *_classes)
	def add_styles(self, *_styles):
		self.attrs['style'] = styles(self.attrs.get('style'), *_styles)

	def __iter__(self):
		yield from _open_tag(self.name, self.attrs)
		yield from yield_children(self.children)
		yield f'</{self.name}>'
class VoidElement(Element):
	'''
		A Void HTML Element (see https://html.spec.whatwg.org/multipage/syntax.html#elements-2)
	'''
	def __init__(self, _name, **attrs):
		super().__init__(_name, **attrs)

	def __iter__(self):
		yield from _open_tag(self.name, self.attrs)
class RawTextElement(Element):
	'''
		A Raw Text HTML Element (script/style)
		(see https://html.spec.whatwg.org/multipage/syntax.html#elements-2)

		These elements cannot have their contents escaped, because html entities are not parsed.

		You should NOT be putting untrusted user content in here.
	'''
	def __init__(self, _name, content='', **attrs):
		super().__init__(_name, **attrs)
		self.content = content

	def __iter__(self):
		yield from _open_tag(self.name, self.attrs)
		yield self.content
		yield f'</{self.name}>'

# Taken from https://html.spec.whatwg.org/multipage/syntax.html June 19, 2020
_VOID_ELEMENTS = [
	'area',
	'base',
	'br',
	'col',
	'embed',
	'hr',
	'img',
	'input',
	'link',
	'meta',
	'param',
	'source',
	'track',
	'wbr',
]
_RAW_TEXT_ELEMENTS = ['script', 'style']
def _smart_element(name):
	if name in _VOID_ELEMENTS:
		return partial(VoidElement, name)
	if name in _RAW_TEXT_ELEMENTS:
		return partial(RawTextElement, name)

	# NOTE - we're ignoring some special element types (the template element, escapable raw text elements) as "normal" -> it makes little to no difference in terms of the html we generate
	return partial(Element, name)

# For convenience, define every known HTML element.
# List adapted from https://developer.mozilla.org/en-US/docs/Web/HTML/Element June 19, 2020
# (doesn't include svg elements)
Html = _smart_element('html')
Body = _smart_element('body')
Base = _smart_element('base')
Head = _smart_element('head')
Link = _smart_element('link')
Meta = _smart_element('meta')
Style = _smart_element('style')
Title = _smart_element('title')
Address = _smart_element('address')
Article = _smart_element('article')
Aside = _smart_element('aside')
Footer = _smart_element('footer')
Header = _smart_element('header')
H1 = _smart_element('h1')
H2 = _smart_element('h2')
H3 = _smart_element('h3')
H4 = _smart_element('h4')
H5 = _smart_element('h5')
H6 = _smart_element('h6')
Hgroup = _smart_element('hgroup')
Main = _smart_element('main')
Nav = _smart_element('nav')
Section = _smart_element('section')
Blockquote = _smart_element('blockquote')
Dd = _smart_element('dd')
Div = _smart_element('div')
Dl = _smart_element('dl')
Dt = _smart_element('dt')
Figcaption = _smart_element('figcaption')
Figure = _smart_element('figure')
Hr = _smart_element('hr')
Li = _smart_element('li')
Main = _smart_element('main')
Ol = _smart_element('ol')
P = _smart_element('p')
Pre = _smart_element('pre')
Ul = _smart_element('ul')
A = _smart_element('a')
Abbr = _smart_element('abbr')
B = _smart_element('b')
Bdi = _smart_element('bdi')
Bdo = _smart_element('bdo')
Br = _smart_element('br')
Cite = _smart_element('cite')
Code = _smart_element('code')
Data = _smart_element('data')
Dfn = _smart_element('dfn')
Em = _smart_element('em')
I = _smart_element('i')
Kbd = _smart_element('kbd')
Mark = _smart_element('mark')
Q = _smart_element('q')
Rb = _smart_element('rb')
Rp = _smart_element('rp')
Rt = _smart_element('rt')
Rtc = _smart_element('rtc')
Ruby = _smart_element('ruby')
S = _smart_element('s')
Samp = _smart_element('samp')
Small = _smart_element('small')
Span = _smart_element('span')
Strong = _smart_element('strong')
Sub = _smart_element('sub')
Sup = _smart_element('sup')
Time = _smart_element('time')
U = _smart_element('u')
Var = _smart_element('var')
Wbr = _smart_element('wbr')
Area = _smart_element('area')
Audio = _smart_element('audio')
Img = _smart_element('img')
Map = _smart_element('map')
Track = _smart_element('track')
Video = _smart_element('video')
Embed = _smart_element('embed')
Iframe = _smart_element('iframe')
Object = _smart_element('object')
Param = _smart_element('param')
Picture = _smart_element('picture')
Source = _smart_element('source')
Canvas = _smart_element('canvas')
Noscript = _smart_element('noscript')
Script = _smart_element('script')
Del = _smart_element('del')
Ins = _smart_element('ins')
Caption = _smart_element('caption')
Col = _smart_element('col')
Colgroup = _smart_element('colgroup')
Table = _smart_element('table')
Tbody = _smart_element('tbody')
Td = _smart_element('td')
Tfoot = _smart_element('tfoot')
Th = _smart_element('th')
Thead = _smart_element('thead')
Tr = _smart_element('tr')
Button = _smart_element('button')
Datalist = _smart_element('datalist')
Fieldset = _smart_element('fieldset')
Form = _smart_element('form')
Input = _smart_element('input')
Label = _smart_element('label')
Legend = _smart_element('legend')
Meter = _smart_element('meter')
Optgroup = _smart_element('optgroup')
Option = _smart_element('option')
Output = _smart_element('output')
Progress = _smart_element('progress')
Select = _smart_element('select')
Textarea = _smart_element('textarea')
Details = _smart_element('details')
Dialog = _smart_element('dialog')
Menu = _smart_element('menu')
Summary = _smart_element('summary')
Slot = _smart_element('slot')
Template = _smart_element('template')
