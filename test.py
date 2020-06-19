from html_generators import *

assert str(Document(
    e.Script('alert("Hello, World!");'),
    e.Body(
        'Direct body text with "<>&\' special characters',
        [
            e.Div(x,div_index=i)
            for i,x in enumerate(['a', 'b', 'c'])
        ],
        e.Input(type="text", value="<&''>"),
        foo="bar",
        _class="a",
    )
)) == '''<!DOCTYPE html>
<script>alert(&quot;Hello, World!&quot;);</script><body foo="bar" class="a">Direct body text with &quot;&lt;&gt;&amp;&#x27; special characters<div>a</div><div div-index="1">b</div><div div-index="2">c</div><input type="text" value="&lt;&amp;&#x27;&#x27;&gt;"></body>'''