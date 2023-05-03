import html_generators as h
from typing import Any

def assert_equal(a, b):
    assert a == b, f'This:\n{a}\nIs not equal to:\n{b}'

assert_equal(h.Content, Any) # documented public type alias

assert_equal(str(h.Input(name='bar')), '<input name="bar">')

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

assert_equal(str(h.Document(h.Body('body'), class_='foo')), '''<!DOCTYPE html>
<html class="foo"><body>body</body></html>''')

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

assert_equal(str(h.template('a')), 'a')
assert_equal(str(h.template('<a')), '&lt;a')
assert_equal(str(h.template(h.MarkSafe('<a>'))), '<a>')
assert_equal(str(h.template(
    '<a{{a}}b{{a}}{{b}}',
    a='A',
    b='B'
)), '&lt;aAbAB')

# Pass a generator to template, make sure it's output is used both times
x = (x for x in [1])
assert_equal(str(h.template('{{x}}{{x}}', x=x)), '11')
# x should be spent - it should have nothing left in it
assert_equal(len(list(x)), 0)

# Missing params unchanged
assert_equal(str(h.template('{{a}}{{b}}')), '{{a}}{{b}}')

# You can pass html
assert_equal(str(h.template('{{a}}', a=h.Br())), '<br>')

# Make sure single-brace works
assert_equal(str(h.template('{a}{b}', a='A', b='B')), 'AB')
assert_equal(str(h.template('{a}{b}')), '{a}{b}')
assert_equal(str(h.template('{a}', a=h.Br())), '<br>')

# Make sure params are escaped
assert_equal(str(h.template('{a}', a='1<2')), '1&lt;2')
# Make sure HtmlGenerator params work as expected
assert_equal(str(h.template('{a}', a=h.Br())), '<br>')

assert_equal(str(h.format('<Please {link_start}click here{link_end}.', link_start=h.A(href='foo').open_tag(), link_end=h.A().close_tag())), '&lt;Please <a href="foo">click here</a>.')

print('Basic tests passed.')