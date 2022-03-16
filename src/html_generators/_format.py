from ._fragment import Fragment
from ._mark_safe import MarkSafe

def format(*template, **context):
    '''
    Useful when injecting html into translatable strings.
    The template gets (conditionally) escaped, as do all of the context values.
    This way, your translator doesn't need to be html-aware.
    
    Ie:
    h.format(
        _('Please {link_start}click here{link_end}.'), 
        link_start=h.A(href=some_path).open_tag(), 
        link_end=h.A().close_tag()
    )

    Will throw KeyError if the template uses any params not given in context.
    '''

    # Escape template, as needed
    template = str(Fragment(template))
    
    return MarkSafe(template.format(**{
        # escape context, as needed
        k: str(Fragment(v))
        for k, v in context.items()
    }))