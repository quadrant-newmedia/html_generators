import html_generators as h

def assert_equal(a, b):
    assert a == b, f'This:\n{a}\nIs not equal to:\n{b}'

assert str(h.Document(
    h.Script('alert("Hello, World!");'),
    h.Body(
        'Direct body text with "<>&\' special characters',
        [
            h.Div(x,div_index=i)
            for i,x in enumerate(['a', 'b', 'c'])
        ],
        h.Input(type="text", value="<&''>"),
        foo="bar",
        _class="a",
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

assert_equal(str(h.Input(__foo_bar_=True)), '<input foo-bar>')

# Ensure children and attribute with value of 0 are rendered
assert_equal(str(h.Div(0, tabindex=0)), '<div tabindex="0">0</div>')

assert_equal(str(h.Img(_class='a').with_classes('b')), '<img class="a b">')
assert_equal(str(h.Div(h.I('a'), _class='a').with_classes('b')), '<div class="a b"><i>a</i></div>')
assert_equal(str(h.Img(style='a: b').with_styles('b: c')), '<img style="a: b; b: c">')