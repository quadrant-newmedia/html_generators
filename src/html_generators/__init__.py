'''
html_generators - functional html generation

Note - all of our submodules (with the exception)
'''
from ._base import Content
from ._document import Document  # noqa
from ._element import Element  # noqa
from ._standard_elements import *  # noqa
from ._standard_elements import __all__ as _all_elements
from ._comment import Comment  # noqa
from ._format import format  # noqa
from ._fragment import Fragment  # noqa
from ._join import Join  # noqa
from ._mark_safe import MarkSafe  # noqa
from ._template import template # noqa
from ._utils import classes, styles  # noqa

# This is for pydoc support, not for "import *" support (which we don't recommend)
__all__ = [
	'Content',
	'Document',
	'Element',
	'Comment',
	'Fragment',
	'format',
	'Join',
	'MarkSafe',
    'template',
	'classes',
	'styles',
	*_all_elements,
]

