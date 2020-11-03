from .base import HTMLGenerator, yield_children

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
            if not first_item :
                yield from self.joiner
            else :
                first_item = False
            yield from child