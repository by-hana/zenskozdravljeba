import json
from django import template

register = template.Library()


@register.filter
def add_class(field, css_class):
    """Add a CSS class to a form field widget."""
    existing = field.field.widget.attrs.get('class', '')
    if existing:
        classes = f'{existing} {css_class}'
    else:
        classes = css_class
    return field.as_widget(attrs={'class': classes})


@register.filter
def add_attr(field, attr_str):
    """Add an attribute to a form field widget. Format: 'attr_name:attr_value'"""
    parts = attr_str.split(':', 1)
    if len(parts) == 2:
        attr_name, attr_value = parts
        return field.as_widget(attrs={attr_name: attr_value})
    return field


@register.filter
def to_json(value):
    """Serialize a value to JSON string."""
    return json.dumps(value)
