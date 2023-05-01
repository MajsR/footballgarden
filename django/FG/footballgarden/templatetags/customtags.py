from django import template
from django.template.defaultfilters import stringfilter

""" Créations de filtre """
# Décorateurs
register = template.Library()


# Définit le décorateur comme un filtre
@register.filter(name='transform')
@stringfilter
def firstChar(value):
    return value[0]


""" Créations de filtre """
from django import template

register = template.Library()


@register.simple_tag()
def hello_world():
    return "Hello World ! "
