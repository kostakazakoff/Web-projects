from django.template import Library
register = Library()

@register.filter(name='data_style')
def format_data_style(date):
    return date.strftime('%A | %d.%b.%Y | %H:%M')