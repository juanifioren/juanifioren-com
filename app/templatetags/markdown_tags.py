from django import template
import markdown2


register = template.Library()

@register.filter
def markdownify(value):
    return markdown2.markdown(value,
        extras=['fenced-code-blocks'])
