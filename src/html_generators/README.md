# html_generators

For anyone who wants to generate html with python.

Inspired by "hyperscript" libraries from the javascript world.

Developed with Django in mind, but designed to work any where. 

## Installation/Quick Start

`pip install html_generators`

```python
import html_generators as h

# A "page template"
def standard_page(title, *content, user=None, page_title=None):
	# h.Document just adds the DOCTYPE line
	return h.Document(
		# h.Title is just an HTML element
		# We have factories defined for all standard HTML elements
		h.Title(title),
		# Keyword arguments become element attributes
		h.Meta(charset='utf-8'),
		h.Link(href=my_static_file('site_styles.css')),
		# Setting an attribute to True will render it with no value
		h.Script(defer=True, src=my_static_file('site_script.js')),

		h.Nav(
			# Elements can have both content (positional args)
			# and attributes (keyword args)
			# At first, it looks odd that an element's attributes are listed 
			# after its content, but you get used to it quickly.
			# With decent syntax highlighting, the attributes stand out nicely
			h.A('Foo', href='/foo/'),
			h.A('Bar', href='/bar/'),

			# Any argument that is False or is None will be skipped.
			# This makes "conditional children" easy
			user and (
				h.A('My Profile', href='/profile/'),
				h.A('Log Out', href='/logout/'),
			)
		),

		h.Main(
			# If the user doesn't provide a custom page title,
			# generate one matching document title
			page_title or h.H1(title),

			content,
		),
	)

# A "chunk template"
def book_section(book):
	return h.Section(
		h.H2(book.title),
		h.P(book.summary),
		# "class" is a reserved word in python, so add a trailing underscore
		# Trailing underscores are trimmed when converting to attribute names
		class_='book',
		# This will render a 'data-id' attribute
		# All underscores (other than trailing) will be converted to hyphens
		data_id=book.id,
	)

# A particular page
def my_books_page(user):
	return standard_page(
		'My Books',
		h.P(h.A('Create new book', href='/books/add/')),
		# Join is not an element - it works like str.join
		# Here we're printing an <hr> between each book section
		h.Join(
			h.Hr(), 
			# This is a generator expression
			# We could also pass a list, but this reduces memory usage
			(
				book_section(book) for book in get_user_books(user)
				if book.published
			)
		),
	)
```

## Background/Philosophy

### Incremental Adoption

You easily can use html_generators to generate all of your site's HTML, or mix it with your existing framework's template system.

HTMLGenerators are completely inter-operable with Django's template system and HTML utility functions, as well as the python "markupsafe" library.

You can pass an HTMLGenerator instance to any of the following, and it will not be escaped:
- django.template.utils.html.format_html
- django.template.utils.html.conditional_escape
- a django template
- markupsafe.escape
- markupsafe.Markup.format()

If you "pre-render" an HTMLGenerator instance (by calling `str()` on it), you'll get a "safe string", which can also be passed to any of the above and won't be escaped.

The converse is also true - you can pass any of the following to an HTMLGenerator, and we'll know not to escape it:
- the result of django's format_html, mark_safe, escape, or conditional_escape
- a markupsafe.Markup instance
 
All of this interoperability is achieved by a fairly straightforward `__html__()` protocol, which is likely also adopted by other python templating/html generation frameworks. 

### Lazy/Streaming

We don't do incremental string concatenation. We produce a single stream of strings, which are only `''.join()`ed by the outermost element. 

This should help with performance and memory usage. Additionally, it means you can actually produce "infinite" HTMLGenerators and pass them to django's StreamingHttpResponse:

```python
import html_generators as h
from itertools import count
from django.http import StreamingHttpResponse

def make_infinite_response():
	return StreamingHttpResponse(h.Document(
		h.Title('Stupid infinite page demo'),
		(
			h.Div(x)
			for x in count(),
		),
	))
```

### Performance

We haven't yet written any performance benchmarks to compare to Django's template system. In our use, it has been fast enough that testing hasn't been warranted (we generate the entirety of each page from scratch on every request - but not yet on any high-traffic sites).

That said, if anyone finds performance to be an issue, or wants to write some benchmarks, we'd be glad to share them here. We have an idea for an optional "pre-compile" step, but don't want to add that complexity to the project if no one needs it.

## Tips/Warnings
### Don't List - Generate!
Consider these two functions:
```python
def books_list(user):
	return h.Div([book_section(book) for book in user.books])
def books_generator(user):
	return h.Div(book_section(book) for book in user.books)
```
The first version creates a (rather useless) list of book sections. The second version is (theoretically) more efficient. It just iterates over the books, and the entire list of sections is never stored in memory. This is the approach we endorse.

### Don't Reuse Instances
HTMLGenerator instances are only intended to be rendered or iterated once. Given the above example, if you did:
```python
books = books_generator(user)
print(books)
print(books)
```
The first print statement would do what you expect, but the second would print an empty div. The generator expression passed to `h.Div` in the `books_generator` function gets "exhausted" the first time you render the result. The second time, there are no more items to generate.

### Altering Elements
Sometimes you need to tweak the output of one your "reusable-component-functions". `Element` provides 3 methods to help with this, which are best demonstrated by example:

```python
# A super simple reusable component
def fancy_button(*content, large=False):
	return h.Button(content, class_="Fancy-button", style=large and 'font-size: 2em;')

# Now imagine we need a fancy button, with some tweaks
print(
	fancy_button('Print this page', large=True)
	# with_attrs lets you add/alter any attributes
	.with_attrs(onclick='window.print()')
	# with_classes will merge the given classes with any already present
	.with_classes('no-print')
	# with_styles will merge the given styles with any already present
	.with_styles('float: right')
)
```

### RawTextElement
`html_generators.Script` and `html_generators.Style` create `RawTextElement` instances. These elements *do not* escape their contents when rendered. These elements are actually defined separately in the HTML spec, and browsers don't parse HTML entities inside them, so there's really nothing we can do. 

You need to make sure the content you pass to them doesn't contain text that would be interpreted as an end tag.

## You Can't Do This With Templates!
### Wrapper Components
Consider this example:
```python
def accordion(sections):
	return h.Div(
		(
			h.Div(
				h.H2(heading, class_='accordion-heading'),
				h.Div(content, class_='accordion-content'),
				class_='accordion-section',
			)
			for heading, content in sections
		),
		class_='accordion',
	)

print(accordion(
	('Section 1', 'Section 1 content...'),
	('Section 2', 'Section 2 content...'),
))
```
There's really no clean way to do this with django templates.

### HTML in Element Attributes

Sometimes it's convenient to put a chunk of HTML inside an element attribute, for consumption by javascript. That HTML needs to be escaped. In a template, you can't just write that HTML (unescaped) in the attribute. With html_generators, you can. HTMLGenerators don't escape other HTMLGenerators that are passed as children, but they escape _everything_ that is passed as an attribute.

```python
h.Button(
	'Click here for details!',
	data_modal=h.Fragment(
		h.H1('Here are the details!', class_='modal-heading'),
		h.P("We'll tell you everything you need to know"),
		...
	),
)
```

In the above example, the Fragment will be converted to a str, and then escaped. 

## API Reference
We haven't yet written/generated a complete API reference, but the code is well documented and fairly straight-forward. We recommend reading the source directly. All "private" interfaces are properly identified with leading underscores - everything else is public and should remain stable between releases.