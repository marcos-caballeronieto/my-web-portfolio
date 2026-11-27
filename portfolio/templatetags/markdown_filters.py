from django import template
import markdown
import re
from django.utils.html import format_html

register = template.Library()


def _wrap_tables(html):
    return re.sub(
        r'<table\b[^>]*>.*?</table>',
        lambda match: f'<div class="markdown-table-wrapper">{match.group(0)}</div>',
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


def _render_markdown_images_in_paragraphs(html):
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    def replace_paragraph(match):
        return re.sub(
            image_pattern,
            lambda image: format_html(
                '<img src="{}" alt="{}">',
                image.group(2),
                image.group(1),
            ),
            match.group(0),
        )

    return re.sub(
        r'<p\b[^>]*>.*?</p>',
        replace_paragraph,
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


@register.filter
def render_markdown(text):
    """
    Renders markdown syntax to HTML if markdown syntax is detected.
    Supports code blocks with syntax highlighting for Python, JavaScript, HTML, CSS, etc.
    Extracts markdown and HTML from CKEditor code blocks and renders them.
    Handles multiple code blocks of different types in the same text.
    
    Args:
        text: Text that may contain markdown, HTML, or other code blocks
        
    Returns:
        HTML string - either rendered markdown/HTML with highlighting or original CKEditor content
    """
    if not text:
        return ''
    
    # Process HTML code blocks from CKEditor: <pre><code class="language-html">...
    html_code_pattern = r'<pre><code class="language-html">(.*?)</code></pre>'
    
    def replace_html_block(match):
        html_content = match.group(1)
        # HTML decode common entities
        html_content = html_content.replace('&lt;', '<')
        html_content = html_content.replace('&gt;', '>')
        html_content = html_content.replace('&amp;', '&')
        html_content = html_content.replace('&quot;', '"')
        return html_content
    
    text = re.sub(html_code_pattern, replace_html_block, text, flags=re.DOTALL)
    
    # Process markdown code blocks from CKEditor: <pre><code class="language-markdown">...
    markdown_code_pattern = r'<pre><code class="language-markdown">(.*?)</code></pre>'
    
    def replace_markdown_block(match):
        markdown_content = match.group(1)
        # HTML decode common entities
        markdown_content = markdown_content.replace('&lt;', '<')
        markdown_content = markdown_content.replace('&gt;', '>')
        markdown_content = markdown_content.replace('&amp;', '&')
        markdown_content = markdown_content.replace('&quot;', '"')
        
        # Render the markdown
        extensions = [
            'markdown.extensions.codehilite',
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.extra',
        ]
        
        extension_configs = {
            'markdown.extensions.codehilite': {
                'guess_lang': True,
                'use_pygments': True,
            }
        }
        
        try:
            return markdown.markdown(markdown_content, extensions=extensions, extension_configs=extension_configs)
        except:
            return markdown.markdown(markdown_content, extensions=extensions)
    
    text = re.sub(markdown_code_pattern, replace_markdown_block, text, flags=re.DOTALL)
    
    # Check if text contains other CKEditor HTML (paragraphs, divs, etc.) - but NOT code blocks
    if '<p>' in text or '<div>' in text or '<ul>' in text or '<ol>' in text:
        # This is CKEditor content with formatting, return as-is
        return _wrap_tables(_render_markdown_images_in_paragraphs(text))
    
    # Check if text contains markdown syntax directly (not in code blocks)
    if (
        '```' in text
        or re.search(r'^[-*]\s', text, re.MULTILINE)
        or re.search(r'^\d+\.\s', text, re.MULTILINE)
        or re.search(
            r'^\s*\|?.+\|.+\|?\s*$\n^\s*\|?\s*:?-{3,}',
            text,
            re.MULTILINE,
        )
    ):
        # This contains markdown syntax, render it
        extensions = [
            'markdown.extensions.codehilite',
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.extra',
        ]
        
        extension_configs = {
            'markdown.extensions.codehilite': {
                'guess_lang': True,
                'use_pygments': True,
            }
        }
        
        try:
            return _wrap_tables(markdown.markdown(text, extensions=extensions, extension_configs=extension_configs))
        except:
            return _wrap_tables(markdown.markdown(text, extensions=extensions))
    
    # Plain text or mixed content, return as-is
    return _wrap_tables(text)

