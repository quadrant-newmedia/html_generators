import html_generators as h
def assert_equal(result, expected):
    assert result == expected, f'Result:\n{result}\nIs not equal to expected:\n{expected}'

from contextlib import contextmanager
@contextmanager
def assert_raises(error):
    try :
        yield
    except error :
        pass
    else :
        raise AssertionError(f'Code did not raise {error} as expected')

import django
from django.conf import settings
from django.http import StreamingHttpResponse
from django.template import Template, Context
from django.template.engine import Engine
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.test_django_settings")

django.setup()

prerendered_br = str(h.Br())

# Ensure we don't escape django safe string
assert_equal(str(h.Fragment(mark_safe('<i>'))), '<i>')
# Ensure django doesn't escape us
assert_equal(conditional_escape(h.I()), '<i></i>')
assert_equal(conditional_escape(prerendered_br), '<br>')
assert_equal(
    format_html('{}', h.Br()),
    '<br>',
)
assert_equal(
    format_html('{}', prerendered_br),
    '<br>',
)
assert_equal(
    Template('{{a}}').render(
        Context({'a': h.Br()})
    ),
    '<br>',
)
assert_equal(
    Template('{{a}}').render(
        Context({'a': prerendered_br})
    ),
    '<br>',
)
# Ensure custom template tags can return us, and we won't be escaped
assert_equal(
    Template(
    	'''{% load hg_tests %}{% a_br %}{% a_prerendered_br %}''',
    ).render(
        Context({})
    ),
    '<br><br>',
)


# "Infinite streaming response"
from itertools import count, islice
infinite_doc = h.Document(h.Div(x) for x in count())
bits = islice(StreamingHttpResponse(infinite_doc), 100)
assert_equal(''.join(b.decode() for b in bits), '''<!DOCTYPE html>
<div>0</div><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div><div>9</div><div>10</div><div>11</div><div>12</div><div>13</div><div>14</div><div>15</div><div>16</div><div>17</div><div>18</div><div>19</div><div>20</div><div>21</div><div>22</div><div>23</div><div>24''')


import datetime
import pytz
from django.utils import timezone
import html_generators.django as hd

dt = pytz.utc.localize(datetime.datetime(2000,1,1,0,0,0))
# passing use_tz=False should not change timezone
assert_equal(hd.date(dt, 'H', use_tz=False), '00')
assert_equal(hd.date(dt, 'e', use_tz=False), 'UTC')
assert_equal(hd.date(dt.astimezone(pytz.timezone('America/Vancouver')), 'H', use_tz=False), '16')
assert_equal(hd.date(dt.astimezone(pytz.timezone('America/Vancouver')), 'e', use_tz=False), 'PST')

# passing no timezone arg should convert to current timezone, we've set default to America/Regina (-6)
assert_equal(hd.date(dt, 'H'), '18')
assert_equal(hd.date(dt, 'e'), 'CST')

# naive dates are allowed, NOT converted
assert_equal(hd.date(datetime.datetime(2000,1,1,0,0,0), 'H'), '00')

# Make sure you can pass date or time
assert_equal(hd.date(datetime.date(2000,1,2), 'j'), '2')
assert_equal(hd.date(datetime.time(1,1,1), 'H'), '01')

assert hd.static('foo.js') == '/static/foo.js'
assert str(hd.Template('foo.html', context=dict(foo='FOO'))) == 'FOO'


print('Django tests passed.')
