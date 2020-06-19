from .base import HTMLGenerator, escape, yield_children
from functools import partial

def _open_tag(name, attrs):
	yield '<'+name
	for key, value in attrs.items() :
		if value == False or value is None :
			continue
		yield ' '
		'''
			lstrip('_')
				this allows you to prefix attribute names with an underscore when those names clash with python built-ins

			replace('_', '-')
				'-' is important in attribute names, '_' is not. You can write python keyword argument names with '_' and they will converted to '-'
		'''
		yield key.lstrip('_').replace('_', '-')
		if value is True :
			continue
		yield f'="{escape(str(value))}"'
	yield '>'

class Element(HTMLGenerator):
	def __init__(self, _name, *_children, **attrs):
		self.name = _name
		self.children = _children
		self.attrs = attrs

	def __iter__(self):
		yield from _open_tag(self.name, self.attrs)
		yield from yield_children(self.children)
		yield f'</{self.name}>'

class VoidElement(HTMLGenerator):
	def __init__(self, _name, **attrs):
		self.name = _name
		self.attrs = attrs

	def __iter__(self):
		yield from _open_tag(self.name, self.attrs)

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
def _smart_element(name):
	if name in _VOID_ELEMENTS:
		return partial(VoidElement, name)
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
