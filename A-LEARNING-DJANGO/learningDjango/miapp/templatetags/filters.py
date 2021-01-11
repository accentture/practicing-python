""" 
    --in this file I will create filters
 """

from django import template

#charging library of templates
register = template.Library()

#======================= this filter will be charged in _layout
#using decorator
                #setting name of filter
@register.filter(name = 'greeting')
def greeting(value) :
    long = ''

    if len(value) >= 8 :
        long = '<p>Tu nombre es muy largo.</p>'

    return f"<h1 style='background:green; color:white; '>Bienvenido {value}</h1> {long}"