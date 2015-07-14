from django import template
import markdown


register = template.Library()

@register.filter
def markdownify(value):
    return markdown.markdown(value)
