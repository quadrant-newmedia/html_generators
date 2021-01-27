from .base import HTMLGenerator, yield_child

class Join(HTMLGenerator):
    '''
        Works similarly to string joining, but the joiner and the output of the iterable need not be strings (they can be other HTMLGenerators, numbers, etc.)
    '''
    def __init__(self, joiner, iterable):
        self.joiner = joiner
        self.iterable = iterable

    def __iter__(self):
        first_item = True
        for child in self.iterable :
            # Skip "explicitly empty" items, just like all other generators
            # Be sure we do NOT add a joiner for this empty item
            if child is None or child is False :
                return

            if not first_item :
                yield from self.joiner
            else :
                first_item = False

            # child could be another HTMLGenerator, iterable, etc.
            yield from yield_child(child)