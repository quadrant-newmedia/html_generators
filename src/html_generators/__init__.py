'''
Note - we recommend importing as:
    import html_generators as h
'''
from .document import Document
from .comment import Comment
# Note - imports Element and VoidElement, as well as all html elements
from .elements import *
from .fragment import Fragment
from .join import Join
from .mark_safe import MarkSafe
from .utils import classes, styles