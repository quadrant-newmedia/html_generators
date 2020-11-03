from .base import HTMLGenerator, yield_children

class Fragment(HTMLGenerator):
    '''
        Represents a fragment of one or more html nodes.

        Note that you generally won't need to use this class, since you can pass iterables directly to Document, Element, etc. 

        If you need to render multiple nodes directly to a string, however, you can use this class.
    '''
    def __init__(self, *children):
        self.children = children

    def __iter__(self):
        yield from yield_children(self.children)