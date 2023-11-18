from django import template

register = template.Library()

@register.filter
def skill(value):
    return 100 - value