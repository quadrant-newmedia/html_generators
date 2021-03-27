import html_generators as h
def assert_equal(a, b):
    assert a == b, f'This:\n{a}\nIs not equal to:\n{b}'

assert str(h.Document(
    h.Script('alert("Hello, World!");'),
    h.Body(
        'Direct body text with "<>&\' special characters',
        (
            h.Div(x,div_index=i)
            for i,x in enumerate(['a', 'b', 'c'])
        ),
        h.Input(type="text", value="<&''>"),
        foo="bar",
        class_="a",
    )
)) == '''<!DOCTYPE html>
<script>alert("Hello, World!");</script><body foo="bar" class="a">Direct body text with &quot;&lt;&gt;&amp;&#x27; special characters<div div-index="0">a</div><div div-index="1">b</div><div div-index="2">c</div><input type="text" value="&lt;&amp;&#x27;&#x27;&gt;"></body>'''

assert_equal(str(h.Fragment(
    'loose text',
    h.Div('a'),
    'more text',
    h.Div('b'),
    'final <> text',
)), '''loose text<div>a</div>more text<div>b</div>final &lt;&gt; text''')

assert_equal(str(h.Comment('My favorite operators are > and <!')), '<!--My favorite operators are > and <!-->')

assert_equal(str(h.Input(foo_bar_=True)), '<input foo-bar>')

# Ensure children and attribute with value of 0 are rendered
assert_equal(str(h.Div(0, tabindex=0)), '<div tabindex="0">0</div>')

assert_equal(str(h.Img(class_='a').with_classes('b')), '<img class="a b">')
assert_equal(str(h.Div(h.I('a'), class_='a').with_classes('b')), '<div class="a b"><i>a</i></div>')
assert_equal(str(h.Img(style='a: b').with_styles('b: c')), '<img style="a: b; b: c">')

# Make sure generator expressions work
assert_equal(str(h.Div(x for x in (1,2,3))), '<div>123</div>')

# Make sure Join works
assert_equal(str(h.Join(h.Br(), [None, 1, None, 2, None, h.I()])), '1<br>2<br><i></i>')

assert_equal(str(h.A(h.MarkSafe('<i>'))), '<a><i></a>')

assert_equal(h.classes(
    'fixed',
    False and 'NOT',
    None and 'NOT',
    True and 'conditional',
), 'fixed conditional')
assert_equal(h.styles(
    'display: block',
    False and 'NOT',
    None and 'NOT',
    True and 'color: green'
), 'display: block; color: green')


import markupsafe
# Ensure we don't escape markupafe.Markup
assert_equal(str(h.Fragment(markupsafe.Markup('<i>'))), '<i>')
# Ensure markupsafe doesn't escape us
assert_equal(markupsafe.escape(h.I()), '<i></i>')
assert_equal(markupsafe.Markup(h.I()), '<i></i>')
assert_equal(
    markupsafe.Markup('a{}'.format(h.Br())),
    'a<br>',
)

from django.conf import settings
from django.http import StreamingHttpResponse
from django.template import Template, Context
from django.template.engine import Engine
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
# Minimal settings allowing us to test template rendering
settings.configure()
# Ensure we don't escape django safe string
assert_equal(str(h.Fragment(mark_safe('<i>'))), '<i>')
# Ensure django doesn't escape us
assert_equal(conditional_escape(h.I()), '<i></i>')
assert_equal(
    format_html('{}', h.Br()),
    '<br>',
)
assert_equal(
    Template('{{a}}', engine=Engine()).render(
        Context({'a': h.Br()})
    ),
    '<br>',
)

# "Infinite streaming response"
from itertools import count, islice
infinite_doc = h.Document(h.Div(x) for x in count())
bits = islice(StreamingHttpResponse(infinite_doc), 100)
assert_equal(''.join(b.decode() for b in bits), '''<!DOCTYPE html>
<div>0</div><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div><div>9</div><div>10</div><div>11</div><div>12</div><div>13</div><div>14</div><div>15</div><div>16</div><div>17</div><div>18</div><div>19</div><div>20</div><div>21</div><div>22</div><div>23</div><div>24''')
