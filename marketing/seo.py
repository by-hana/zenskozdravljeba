import re
from django.utils.text import Truncator


def extract_first_image(html):
    if not html:
        return None
    match = re.search(r'<img[^>]+src="([^"]+)"', html)
    if not match:
        return None
    return match.group(1).strip()


def extract_first_paragraph(html, limit=160):
    if not html:
        return ''
    match = re.search(r'<p[^>]*>(.*?)</p>', html, flags=re.I | re.S)
    if not match:
        return ''
    raw = re.sub(r'<[^>]+>', '', match.group(1)).strip()
    return Truncator(raw).chars(limit)


def extract_first_image_from_blocks(blocks_json):
    if not blocks_json:
        return None
    blocks = blocks_json.get('blocks', []) if isinstance(blocks_json, dict) else blocks_json
    for block in blocks:
        if block.get('type') == 'rich_text':
            content = block.get('content', {})
            if isinstance(content, dict):
                for b in content.get('blocks', []):
                    if b.get('type') == 'image':
                        return b.get('data', {}).get('file', {}).get('url')
        if block.get('type') == 'image_gallery':
            images = block.get('images', [])
            if images and images[0].get('src'):
                return images[0]['src']
    return None


def build_seo_payload(obj, request=None):
    html = getattr(obj, 'body_html', '') or ''
    if not html:
        html = getattr(obj, 'blocks_html', '') or ''

    title = obj.seo_title or obj.title
    description = obj.seo_description or extract_first_paragraph(html)
    og_title = obj.og_title or title
    og_description = obj.og_description or description

    image = None
    if obj.og_image:
        image = obj.og_image
    elif obj.twitter_image:
        image = obj.twitter_image
    elif getattr(obj, 'primary_image', None):
        image = obj.primary_image
    elif getattr(obj, 'cover_image', None):
        image = obj.cover_image
    else:
        image = extract_first_image(html)
        if not image:
            image = extract_first_image_from_blocks(getattr(obj, 'blocks_json', None))

    payload = {
        'title': title,
        'description': description,
        'og_title': og_title,
        'og_description': og_description,
        'image': image,
    }
    if request:
        payload['url'] = request.build_absolute_uri(obj.get_absolute_url())
        if payload.get('image') and not payload['image'].startswith('http'):
            payload['image'] = request.build_absolute_uri(payload['image'])
    return payload


def build_article_schema(post, request=None):
    """
    Build Article + MedicalWebPage JSON-LD schema dict for a blog post.
    Returns a dict suitable for json.dumps() and embedding as ld+json.
    """
    schema = {
        "@context": "https://schema.org",
        "@type": ["Article", "MedicalWebPage"],
        "headline": post.title,
        "inLanguage": "bs",
        "publisher": {
            "@type": "Organization",
            "name": "ŽenskoZdravlje.ba"
        },
        "author": {
            "@type": "Person",
            "name": post.author_name or "ŽenskoZdravlje.ba"
        },
    }
    if post.publish_at:
        schema["datePublished"] = post.publish_at.isoformat()
    schema["dateModified"] = post.updated_at.isoformat()
    if post.cover_image:
        schema["image"] = post.cover_image
    if post.seo_description:
        schema["description"] = post.seo_description
    if request:
        schema["url"] = request.build_absolute_uri(post.get_absolute_url())
    return schema
