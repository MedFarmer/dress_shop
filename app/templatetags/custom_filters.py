from django import template

register = template.Library()

@register.filter
def thousands_with_spaces(value):
    try:
        # Convert the input to an integer if it's a string
        value = int(value) if isinstance(value, str) else value
        # Format the number with spaces for thousands separator
        formatted_value = "{:,}".format(value).replace(",", " ")
        return formatted_value
    except (ValueError, TypeError):
        return value
