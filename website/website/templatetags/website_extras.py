from django import template
import markdown as md
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


register = template.Library()

@register.filter(needs_autoescape=True)
def markdown(value, autoescape=True):
    tailwindCssPrefix = '''
    
    
            
    '''


    return mark_safe(md.markdown(value))

@register.filter()
def MB(value, autoescape=False):
    return str(int(value)/1000)
