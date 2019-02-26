from django import template

register = template.Library()


@register.filter
def smult(number, char):
    return int(number) * char
