from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def dark_mode_link():
    return '<link rel="stylesheet" id="theme-style-dark" defer>'