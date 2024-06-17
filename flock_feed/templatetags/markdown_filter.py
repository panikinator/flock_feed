from django import template 
import markdown
md = markdown.Markdown(extensions=["fenced_code"])

  
register = template.Library() 
  
@register.filter() 
def render_markdown(value): 
    return md.convert(value)
