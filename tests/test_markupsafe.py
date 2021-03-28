import html_generators as h
def assert_equal(a, b):
    assert a == b, f'This:\n{a}\nIs not equal to:\n{b}'

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

print('markupsafe tests passed.')