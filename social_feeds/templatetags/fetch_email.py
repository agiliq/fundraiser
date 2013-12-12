from django import template

register = template.Library()


@register.filter
def fetch_email(value):
    if value:
        values = value.split(' ')
        for val in values:
            if '@' in val:
                return val
