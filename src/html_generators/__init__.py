'''
html_generators - functional html generation
'''
from ._internals.document import Document  # noqa
from ._internals.element import Element  # noqa
from ._internals.standard_elements import *  # noqa
from ._internals.standard_elements import __all__ as _all_elements
from ._internals.comment import Comment  # noqa
from ._internals.fragment import Fragment  # noqa
from ._internals.join import Join  # noqa
from ._internals.mark_safe import MarkSafe  # noqa
from ._internals.utils import classes, styles  # noqa

# This is for pydoc support, not for "import *" support
__all__ = [
	'Document',
	'Element',
	'Comment',
	'Fragment',
	'Join',
	'MarkSafe',
	'classes',
	'styles',
] + _all_elements