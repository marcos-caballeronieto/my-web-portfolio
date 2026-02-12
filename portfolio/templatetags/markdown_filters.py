from django import template
import markdown
import re

register = template.Library()

@register.filter
def render_markdown(text):
    """
    Renders markdown syntax to HTML if markdown syntax is detected.
    Supports code blocks with syntax highlighting for Python, JavaScript, HTML, CSS, etc.
    If CKEditor HTML is detected, returns it as-is.
    
    Args:
        text: Text that may contain markdown or HTML
        
    Returns:
        HTML string - either rendered markdown with highlighting or original CKEditor HTML
    """
    if not text:
        return ''
    
    # Check if text contains CKEditor HTML (paragraphs, divs, etc.)
    # But exclude code blocks which should be rendered
    if '<p>' in text or '<div>' in text:
        # Check if it's just a simple <pre> or <code> tag (from CKEditor code block)
        if not (text.strip().startswith('<pre') or text.strip().startswith('<code')):
            # This is CKEditor content, return as-is
            return text
    
    # Check if text contains markdown code blocks or formatting
    if '```' in text or re.search(r'^[-*]\s', text, re.MULTILINE) or re.search(r'^\d+\.\s', text, re.MULTILINE):
        # This contains markdown syntax, render it with syntax highlighting
        extensions = [
            'markdown.extensions.codehilite',
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.extra',
        ]
        
        # Set code highlighting config
        extension_configs = {
            'markdown.extensions.codehilite': {
                'guess_lang': True,
                'use_pygments': True,
            }
        }
        
        try:
            return markdown.markdown(text, extensions=extensions, extension_configs=extension_configs)
        except:
            # Fallback if Pygments is not available
            return markdown.markdown(text, extensions=extensions)
    
    # Plain text or mixed content, return as-is
    return text

