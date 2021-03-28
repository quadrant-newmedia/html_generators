from django import template
import html_generators as h

prerendered_br = str(h.Br())

register = template.Library()
@register.simple_tag
def a_br():
	return h.Br()

@register.simple_tag
def a_prerendered_br():
	return prerendered_br