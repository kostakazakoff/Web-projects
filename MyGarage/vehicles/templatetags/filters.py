from django.template import Library
register = Library()

@register.filter(name='data_style')
def format_data_style(date):
    return date.strftime('%A | %d.%b.%Y | %H:%M')

@register.filter(name='order_vehicles')
def order_vehicles(vehicles, criteria):
    return vehicles.order_by(criteria)