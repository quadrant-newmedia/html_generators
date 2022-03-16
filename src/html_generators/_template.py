import re
from ._base import HTMLGenerator, escape
from ._fragment import Fragment

class _LazyString:
    '''
    Intended to wrap an HTMLGenerator, stringify it lazily and only once, even if used as a string multiple times.

    In case source is a "one-shot" generator.

    TODO - export this? Could be useful elsewhere
    '''
    def __init__(self, source):
        self.source = source
        self.string = None

    def __str__(self):
        if self.string is None :
            self.string = str(self.source)
        return self.string

class template(HTMLGenerator):
    '''
    Note - class name is lowercase because html_generators.Template is already used to create <template> html elements.

    Best explained by 2 intended use cases.

    1. Translatable strings, with html replacements:
        h.template(
            # xgettext:python-brace-format
            _('You have been paired with {partner}.'),
            partner=h.A('John Smith', href='mailto:...'),
        )
        Here, you have a translatable string which we escape.
        After the translated string is escaped, we do the replacements
        (which might contain html, as they do here).

    2. Trusted user-generated html templates
        h.template(
            h.MarkSafe(get_welcome_email_template_from_db()),
            home_page_link=h.A(...),
            user_name='John Smith',
        )

    Note on translations:
    Our replacement pattern is compatible with python-brace-format strings
    You may want to add this comment on the line above your translatable strings:
    # xgettext:python-brace-format
    (but xgettext usually identifies them properly)
    '''
    def __init__(self, template, **context):
        self.template = template

        # Stringify (and escape) context lazily, and only once
        # Values could be "one-shot" generators, but they should produce same result if used multiple times in template
        self.context = {
            key: _LazyString(Fragment(value))
            for key, value in context.items()
        }

    def __iter__(self):
        # escape template, unless it's already a "safe" object
        template = str(Fragment(self.template))

        def get_replacement(match):
            try :
                value = self.context[match.group(1)]
            except KeyError :
                # Return the entire match, including wrapping braces
                return match.group()
            else :
                return str(value)

        # Backward compatibility. Handle {{pattern}}.
        # TODO - drop this in v3.
        template = re.sub(r'{{([a-zA-Z0-9_]+)}}', get_replacement, template)
        # Replace {pattern}. xgettext will identify these as python-brace-format strings, which is very helpful to ensure proper translation.
        template = re.sub(r'{([a-zA-Z0-9_]+)}', get_replacement, template)
        yield template
