from django.template import Library
register = Library()


@register.simple_tag(name='kwargs_string')
def get_string_of_kwargs(**kwargs):
    pass


@register.inclusion_tag(filename='tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args
    }
    return context
