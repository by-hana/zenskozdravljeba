import re
from html import escape

from bs4 import BeautifulSoup, Comment


ALLOWED_TAGS = {
    'p', 'strong', 'em', 'b', 'i', 'u', 's', 'a', 'ul', 'ol', 'li', 'br', 'hr',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 'pre', 'figure',
    'figcaption', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'span', 'div'
}

ALLOWED_ATTRS = {
    'a': {'href', 'title', 'target', 'rel'},
    'img': {'src', 'alt', 'title', 'width', 'height', 'loading'},
    'div': {'class'},
    'span': {'class'},
    'table': {'class'},
    'thead': {'class'},
    'tbody': {'class'},
    'tr': {'class'},
    'th': {'class'},
    'td': {'class'},
    'figure': {'class'},
    'figcaption': {'class'},
    'p': {'class'},
    'blockquote': {'class'},
    'h1': {'class'}, 'h2': {'class'}, 'h3': {'class'},
    'h4': {'class'}, 'h5': {'class'}, 'h6': {'class'},
}


def render_lexical_json(payload):
    if not payload:
        return ''
    root = payload.get('root', {})
    children = root.get('children', [])
    return ''.join(_render_node(child) for child in children)


def _render_node(node):
    node_type = node.get('type', '')
    if node_type == 'paragraph':
        children_html = ''.join(_render_node(c) for c in node.get('children', []))
        return _wrap('p', children_html)
    elif node_type == 'heading':
        tag = node.get('tag', 'h2')
        children_html = ''.join(_render_node(c) for c in node.get('children', []))
        return _wrap(tag, children_html)
    elif node_type in ('text', 'extended-text'):
        text = escape(node.get('text', ''))
        fmt = node.get('format', 0)
        if fmt & 1:
            text = f'<strong>{text}</strong>'
        if fmt & 2:
            text = f'<em>{text}</em>'
        return text
    elif node_type == 'linebreak':
        return '<br>'
    return ''


def render_editorjs(payload):
    if not payload:
        return ''
    blocks = payload.get('blocks', []) if isinstance(payload, dict) else []
    html = ''
    for block in blocks:
        block_type = block.get('type')
        data = block.get('data', {})
        if block_type == 'paragraph':
            html += _wrap('p', _sanitize_inline_html(data.get('text', '')))
        elif block_type == 'header':
            level = str(data.get('level', 2))
            tag = f"h{level}"
            html += _wrap(tag, _sanitize_inline_html(data.get('text', '')))
        elif block_type == 'list':
            html += _render_editorjs_list(data)
        elif block_type == 'quote':
            html += _wrap('blockquote', _sanitize_inline_html(data.get('text', '')))
        elif block_type == 'table':
            html += _render_editorjs_table(data)
        elif block_type == 'code':
            html += _wrap('pre', _wrap('code', escape(data.get('code', ''))))
        elif block_type == 'delimiter':
            html += '<hr />'
        elif block_type == 'warning':
            title = _sanitize_inline_html(data.get('title', ''))
            message = _sanitize_inline_html(data.get('message', ''))
            html += _wrap('div', _wrap('h4', title) + _wrap('p', message), class_name='cms-callout')
    return html


def _wrap(tag, content, class_name=None):
    if tag not in ALLOWED_TAGS:
        return ''
    attrs = ''
    if class_name:
        attrs = f' class="{class_name}"'
    return f'<{tag}{attrs}>{content}</{tag}>'


def sanitize_html(html):
    if not html:
        return ''

    # Preserve trusted code blocks
    code_blocks = []

    def _stash(m):
        code_blocks.append(m.group(0))
        return f"__TRUSTED_CODE_BLOCK_{len(code_blocks) - 1}__"

    html = re.sub(
        r'<!--TRUSTED_CODE_START-->.*?<!--TRUSTED_CODE_END-->',
        _stash,
        html,
        flags=re.S,
    )

    html = re.sub(r'<\s*script[^>]*>.*?<\s*/\s*script\s*>', '', html, flags=re.I | re.S)
    html = re.sub(r'on\w+\s*=\s*"[^"]*"', '', html, flags=re.I)

    for i, block in enumerate(code_blocks):
        html = html.replace(f"__TRUSTED_CODE_BLOCK_{i}__", block)

    return html


def _sanitize_inline_html(html):
    if not html:
        return ''
    soup = BeautifulSoup(html, 'html.parser')
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.find_all(True):
        if tag.name not in ALLOWED_TAGS:
            tag.unwrap()
            continue
        allowed = ALLOWED_ATTRS.get(tag.name, set())
        tag.attrs = {key: value for key, value in tag.attrs.items() if key in allowed}
    return str(soup)


def _render_editorjs_list(data):
    style = data.get('style', 'unordered')
    tag = 'ol' if style == 'ordered' else 'ul'
    items = ''.join(_wrap('li', _sanitize_inline_html(item)) for item in data.get('items', []))
    return _wrap(tag, items)


def _render_editorjs_table(data):
    rows = data.get('content', [])
    body_rows = ''.join(_wrap('tr', ''.join(_wrap('td', _sanitize_inline_html(cell)) for cell in row)) for row in rows)
    return _wrap('table', _wrap('tbody', body_rows), class_name='cms-table')
