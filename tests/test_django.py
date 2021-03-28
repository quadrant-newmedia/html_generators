import html_generators as h
def assert_equal(a, b):
    assert a == b, f'This:\n{a}\nIs not equal to:\n{b}'

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

# TODO - ensure we're not escaped when returned from template tag
# Ensure we're not escaped even if "pre-rendered"

# "Infinite streaming response"
from itertools import count, islice
infinite_doc = h.Document(h.Div(x) for x in count())
bits = islice(StreamingHttpResponse(infinite_doc), 100)
assert_equal(''.join(b.decode() for b in bits), '''<!DOCTYPE html>
<div>0</div><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div><div>9</div><div>10</div><div>11</div><div>12</div><div>13</div><div>14</div><div>15</div><div>16</div><div>17</div><div>18</div><div>19</div><div>20</div><div>21</div><div>22</div><div>23</div><div>24''')

print('Django tests passed.')