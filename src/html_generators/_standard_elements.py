'''
Shortcut factories for all (non-svg) standard HTML elements
'''
from ._element import Element, VoidElement, RawTextElement

# Note - we add items to this dynamically, below
__all__ = []

# Taken from https://html.spec.whatwg.org/multipage/syntax.html June 19, 2020
VOID_ELEMENTS = [
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
RAW_TEXT_ELEMENTS = ['script', 'style']

def registered_factory(element_name):
	__all__.append(element_name.title())

	# NOTE - we're ignoring some special element types (the template element, escapable raw text elements) and treating them as "normal" -> it makes little to no difference in terms of the html we generate
	# escapable raw text elements (ie. <title>) can't have child elements. We _could_ implement those, and do extra validation, but it's not really our job to be an HTML validator - users still have to be aware of which elements are allowed inside which other elements
	type_ = (
		VoidElement if element_name in VOID_ELEMENTS 
		else RawTextElement if element_name in RAW_TEXT_ELEMENTS
		else Element
	)

	def factory(*args, **kwargs):
		return type_(element_name, *args, **kwargs)
	factory.__name__ = element_name
	factory.__doc__ = f'''<{element_name}> {type_.__name__} factory.'''
	return factory

# List adapted from https://developer.mozilla.org/en-US/docs/Web/HTML/Element June 19, 2020
# (doesn't include svg elements)
Html = registered_factory('html')
Body = registered_factory('body')
Base = registered_factory('base')
Head = registered_factory('head')
Link = registered_factory('link')
Meta = registered_factory('meta')
Style = registered_factory('style')
Title = registered_factory('title')
Address = registered_factory('address')
Article = registered_factory('article')
Aside = registered_factory('aside')
Footer = registered_factory('footer')
Header = registered_factory('header')
H1 = registered_factory('h1')
H2 = registered_factory('h2')
H3 = registered_factory('h3')
H4 = registered_factory('h4')
H5 = registered_factory('h5')
H6 = registered_factory('h6')
Hgroup = registered_factory('hgroup')
Main = registered_factory('main')
Nav = registered_factory('nav')
Section = registered_factory('section')
Blockquote = registered_factory('blockquote')
Dd = registered_factory('dd')
Div = registered_factory('div')
Dl = registered_factory('dl')
Dt = registered_factory('dt')
Figcaption = registered_factory('figcaption')
Figure = registered_factory('figure')
Hr = registered_factory('hr')
Li = registered_factory('li')
Main = registered_factory('main')
Ol = registered_factory('ol')
P = registered_factory('p')
Pre = registered_factory('pre')
Ul = registered_factory('ul')
A = registered_factory('a')
Abbr = registered_factory('abbr')
B = registered_factory('b')
Bdi = registered_factory('bdi')
Bdo = registered_factory('bdo')
Br = registered_factory('br')
Cite = registered_factory('cite')
Code = registered_factory('code')
Data = registered_factory('data')
Dfn = registered_factory('dfn')
Em = registered_factory('em')
I = registered_factory('i')
Kbd = registered_factory('kbd')
Mark = registered_factory('mark')
Q = registered_factory('q')
Rb = registered_factory('rb')
Rp = registered_factory('rp')
Rt = registered_factory('rt')
Rtc = registered_factory('rtc')
Ruby = registered_factory('ruby')
S = registered_factory('s')
Samp = registered_factory('samp')
Small = registered_factory('small')
Span = registered_factory('span')
Strong = registered_factory('strong')
Sub = registered_factory('sub')
Sup = registered_factory('sup')
Time = registered_factory('time')
U = registered_factory('u')
Var = registered_factory('var')
Wbr = registered_factory('wbr')
Area = registered_factory('area')
Audio = registered_factory('audio')
Img = registered_factory('img')
Map = registered_factory('map')
Track = registered_factory('track')
Video = registered_factory('video')
Embed = registered_factory('embed')
Iframe = registered_factory('iframe')
Object = registered_factory('object')
Param = registered_factory('param')
Picture = registered_factory('picture')
Source = registered_factory('source')
Canvas = registered_factory('canvas')
Noscript = registered_factory('noscript')
Script = registered_factory('script')
Del = registered_factory('del')
Ins = registered_factory('ins')
Caption = registered_factory('caption')
Col = registered_factory('col')
Colgroup = registered_factory('colgroup')
Table = registered_factory('table')
Tbody = registered_factory('tbody')
Td = registered_factory('td')
Tfoot = registered_factory('tfoot')
Th = registered_factory('th')
Thead = registered_factory('thead')
Tr = registered_factory('tr')
Button = registered_factory('button')
Datalist = registered_factory('datalist')
Fieldset = registered_factory('fieldset')
Form = registered_factory('form')
Input = registered_factory('input')
Label = registered_factory('label')
Legend = registered_factory('legend')
Meter = registered_factory('meter')
Optgroup = registered_factory('optgroup')
Option = registered_factory('option')
Output = registered_factory('output')
Progress = registered_factory('progress')
Select = registered_factory('select')
Textarea = registered_factory('textarea')
Details = registered_factory('details')
Dialog = registered_factory('dialog')
Menu = registered_factory('menu')
Summary = registered_factory('summary')
Slot = registered_factory('slot')
Template = registered_factory('template')
