from .base import HTMLGenerator
from django.template.loader import render_to_string

class DjangoTemplate(HTMLGenerator):
    def __init__(self, template_name, request=None, context=None, using=None):
        self.template_name = template_name
        self.request = request
        self.context = context
        self.using = using

    def __iter__(self):
        yield render_to_string(self.template_name, context=self.context, request=self.request, using=self.using)
