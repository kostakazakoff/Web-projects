from django.template import Library
from datetime import datetime

register = Library()

@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }
    return context
