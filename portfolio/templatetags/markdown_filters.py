from django import template
import markdown
import re
from django.utils.html import format_html
from django.utils.html import strip_tags
from html import unescape

register = template.Library()


def _wrap_tables(html):
    return re.sub(
        r'<table\b[^>]*>.*?</table>',
        lambda match: f'<div class="markdown-table-wrapper">{match.group(0)}</div>',
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


def _normalize_markdown_tables(text):
    lines = text.splitlines()
    normalized = []
    index = 0

    def split_row(line):
        if '|' not in line:
            return None
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        return cells if len(cells) > 1 else None

    while index < len(lines):
        header = split_row(lines[index])
        separator = split_row(lines[index + 1]) if index + 1 < len(lines) else None
        if (
            not header
            or not separator
            or len(separator) != len(header)
            or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in separator)
        ):
            normalized.append(lines[index])
            index += 1
            continue

        if normalized and normalized[-1].strip():
            normalized.append('')
        normalized.extend((lines[index], lines[index + 1]))
        index += 2
        while index < len(lines):
            row = split_row(lines[index])
            if not row or len(row) != len(header):
                break
            normalized.append(lines[index])
            index += 1
        if index < len(lines) and lines[index].strip():
            normalized.append('')

    return '\n'.join(normalized)


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


def _render_markdown_tables_in_paragraphs(html):
    paragraphs = list(
        re.finditer(r'<p\b[^>]*>(.*?)</p>', html, flags=re.DOTALL | re.IGNORECASE)
    )

    def get_row(paragraph):
        content = unescape(strip_tags(paragraph.group(1))).strip()
        if '|' not in content:
            return None
        cells = [cell.strip() for cell in content.strip('|').split('|')]
        return cells if len(cells) > 1 else None

    replacements = []
    index = 0
    while index < len(paragraphs):
        header = get_row(paragraphs[index])
        if not header or index + 1 >= len(paragraphs):
            index += 1
            continue

        separator = get_row(paragraphs[index + 1])
        gap = html[paragraphs[index].end():paragraphs[index + 1].start()]
        if (
            gap.strip()
            or not separator
            or len(separator) != len(header)
            or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in separator)
        ):
            index += 1
            continue

        end_index = index + 1
        rows = [header, separator]
        while end_index + 1 < len(paragraphs):
            gap = html[paragraphs[end_index].end():paragraphs[end_index + 1].start()]
            row = get_row(paragraphs[end_index + 1])
            if gap.strip() or not row:
                break
            rows.append(row)
            end_index += 1

        markdown_table = '\n'.join('| ' + ' | '.join(row) + ' |' for row in rows)
        rendered_table = markdown.markdown(markdown_table, extensions=['tables'])
        replacements.append((
            paragraphs[index].start(),
            paragraphs[end_index].end(),
            rendered_table,
        ))
        index = end_index + 1

    for start, end, rendered_table in reversed(replacements):
        html = html[:start] + rendered_table + html[end:]
    return html


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
        markdown_content = _normalize_markdown_tables(markdown_content)
        
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
        text = _render_markdown_tables_in_paragraphs(text)
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
            text = _normalize_markdown_tables(text)
            return _wrap_tables(markdown.markdown(text, extensions=extensions, extension_configs=extension_configs))
        except:
            text = _normalize_markdown_tables(text)
            return _wrap_tables(markdown.markdown(text, extensions=extensions))
    
    # Plain text or mixed content, return as-is
    return _wrap_tables(text)

