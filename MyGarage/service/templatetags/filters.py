from django.template import Library
register = Library()

@register.filter(name='date_style')
def format_date_style(date):
    return date.strftime('%A | %d.%b.%Y')