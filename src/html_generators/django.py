'''
html_generators.django

Utilities for using html_generators within a django project.
This is the only module within html_generators that has any django dependencies.
'''

from .base import HTMLGenerator
from django.template.loader import render_to_string

class DjangoTemplate(HTMLGenerator):
    '''
        An HTMLGenerator which renders a given template with given request/context.

        You could just call render_to_string in your own code, but then:
            - you'd have to wrap it in html_generators.MarkSafe
            - string generation would be done "out of order"

        That second issue is mostly just academic, but it could have some slight performance ramifications if you were generating a large streaming response. With html_generators, we're trying to be consistent about rendering all content "just in time", and this utility helps achieve that.
    '''
    def __init__(self, template_name, request=None, context=None, using=None):
        self.template_name = template_name
        self.request = request
        self.context = context
        self.using = using

    def __iter__(self):
        yield render_to_string(self.template_name, context=self.context, request=self.request, using=self.using)
