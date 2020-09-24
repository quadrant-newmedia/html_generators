from .base import HTMLGenerator

class Comment(HTMLGenerator):
    def __init__(self, content):
        self.content = content

    def __iter__(self):
        yield '<!--'
        yield self.content
        yield '-->'