from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Page, Post, NavMenu, Footer, Category, BlogPost
from .seo import build_seo_payload


def marketing_home(request):
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    recent_posts = [p for p in Post.objects.filter(status__in=['published', 'scheduled']).order_by('-publish_at')[:3] if p.is_published]
    return render(request, 'marketing/home.html', {
        'nav_menu': nav,
        'footer': footer,
        'recent_posts': recent_posts,
        'seo': {
            'title': 'ZenskoZdravlje.ba: Reproduktivno zdravlje, Ginekologija, Hormoni i Mentalno zdravlje',
            'description': 'Besplatni informativni portal o zenskom zdravlju. Strucni clanci o hormonima, menstrualnom ciklusu, PCOS-u, ginekologiji, trudnoci, ishrani, suplementima i mentalnom zdravlju.',
            'og_title': 'ZenskoZdravlje.ba: Pouzdane informacije o zenskom zdravlju',
            'og_description': 'Strucni, provjereni clanci o svim aspektima zenskog zdravlja. Hormoni, ginekologija, trudnoca, ishrana i mentalno zdravlje.',
            'image': None,
            'url': request.build_absolute_uri('/'),
        },
    })


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if not page.is_published:
        raise Http404()
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    return render(request, 'marketing/page.html', {
        'page': page,
        'nav_menu': nav,
        'footer': footer,
        'seo': build_seo_payload(page, request=request),
    })


# Maps cluster slugs → category slugs (where they differ)
_CLUSTER_TO_CATEGORY = {
    'koza-kosa-hormoni':       'koza-kosa-i-hormoni',
    'plodnost-trudnoca':       'plodnost-i-trudnoca',
    'pcos-hormonski-poremecaji': 'pcos-i-hormonski-poremecaji',
}
# Reverse: category slug → cluster slug
_CATEGORY_TO_CLUSTER = {v: k for k, v in _CLUSTER_TO_CATEGORY.items()}


def blog_index(request):
    category_slug = request.GET.get('category', '')

    # Existing Post objects
    posts_qs = Post.objects.filter(status__in=['published', 'scheduled']).order_by('-publish_at')
    if category_slug:
        posts_qs = posts_qs.filter(categories__slug=category_slug)
    posts = [post for post in posts_qs if post.is_published]

    # AI BlogPost objects — match by cluster when a category is selected
    ai_posts_qs = BlogPost.objects.filter(status='published').order_by('-published_at')
    if category_slug:
        cluster_slug = _CATEGORY_TO_CLUSTER.get(category_slug, category_slug)
        ai_posts_qs = ai_posts_qs.filter(cluster=cluster_slug)

    categories = Category.objects.all()
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()

    return render(request, 'marketing/blog_index.html', {
        'posts': posts,
        'ai_posts': list(ai_posts_qs),
        'categories': categories,
        'active_category': category_slug,
        'nav_menu': nav,
        'footer': footer,
        'seo': {
            'title': 'Blog o ženskom zdravlju | ŽenskoZdravlje.ba',
            'description': 'Stručni članci i informacije o ženskom zdravlju: PCOS, hormoni, ginekologija, trudnoća, ishrana i mentalno zdravlje.',
            'og_title': 'Blog o ženskom zdravlju | ŽenskoZdravlje.ba',
            'og_description': 'Stručni članci o ženskom zdravlju: PCOS, hormoni, ginekologija, trudnoća i mentalno zdravlje.',
            'image': None,
        },
    })


def blog_post_detail(request, slug):
    # Check AI BlogPost first
    ai_post = BlogPost.objects.filter(slug=slug, status='published').first()
    if ai_post:
        nav = NavMenu.objects.filter(name='Primary').first()
        footer = Footer.objects.first()
        # Related posts from same cluster
        related_posts = list(
            BlogPost.objects.filter(cluster=ai_post.cluster, status='published')
            .exclude(slug=slug)
            .order_by('-published_at')[:4]
        )
        return render(request, 'marketing/ai_blog_post.html', {
            'post': ai_post,
            'nav_menu': nav,
            'footer': footer,
            'related_posts': related_posts,
            'seo': {
                'title': ai_post.meta_title or ai_post.title,
                'description': ai_post.meta_description,
                'og_title': ai_post.meta_title or ai_post.title,
                'og_description': ai_post.meta_description,
                'url': request.build_absolute_uri(f'/blog/{slug}/'),
                'image': None,
            },
        })

    # Fallback to old Post model
    post = get_object_or_404(Post, slug=slug)
    if not post.is_published:
        raise Http404()
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    return render(request, 'marketing/blog_post.html', {
        'post': post,
        'nav_menu': nav,
        'footer': footer,
        'seo': build_seo_payload(post, request=request),
    })


def category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_qs = Post.objects.filter(status__in=['published', 'scheduled'], categories=category).order_by('-publish_at')
    posts = [p for p in posts_qs if p.is_published]
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    return render(request, 'marketing/category.html', {
        'category': category,
        'posts': posts,
        'nav_menu': nav,
        'footer': footer,
        'seo': {
            'title': f'{category.name} - ZenskoZdravlje.ba',
            'description': f'Clanci o temi {category.name} na ZenskoZdravlje.ba - pouzdane informacije o zenskom zdravlju.',
            'og_title': category.name,
            'og_description': f'Clanci o temi {category.name}',
            'url': request.build_absolute_uri(f'/kategorija/{category.slug}/'),
        },
    })


def sitemap_xml(request):
    base = request.build_absolute_uri('/').rstrip('/')
    urls = []
    urls.append({'loc': f'{base}/', 'changefreq': 'weekly', 'priority': '1.0'})
    urls.append({'loc': f'{base}/blog/', 'changefreq': 'daily', 'priority': '0.8'})

    for category in Category.objects.all():
        urls.append({
            'loc': f'{base}/kategorija/{category.slug}/',
            'changefreq': 'weekly',
            'priority': '0.7',
        })

    for page in Page.objects.filter(status__in=['published', 'scheduled']).order_by('title'):
        if not page.is_published:
            continue
        urls.append({
            'loc': f'{base}/{page.slug}/',
            'lastmod': page.updated_at.strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.7',
        })

    for post in Post.objects.filter(status__in=['published', 'scheduled']).order_by('-publish_at'):
        if not post.is_published:
            continue
        urls.append({
            'loc': f'{base}/blog/{post.slug}/',
            'lastmod': post.updated_at.strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.6',
        })

    for ai_post in BlogPost.objects.filter(status='published').order_by('-published_at'):
        urls.append({
            'loc': f'{base}/blog/{ai_post.slug}/',
            'lastmod': ai_post.updated_at.strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.7' if ai_post.is_pillar else '0.6',
        })

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in urls:
        lines.append('  <url>')
        lines.append(f'    <loc>{entry["loc"]}</loc>')
        if 'lastmod' in entry:
            lines.append(f'    <lastmod>{entry["lastmod"]}</lastmod>')
        lines.append(f'    <changefreq>{entry["changefreq"]}</changefreq>')
        lines.append(f'    <priority>{entry["priority"]}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')

    return HttpResponse('\n'.join(lines), content_type='application/xml')


def robots_txt(request):
    base = request.build_absolute_uri('/').rstrip('/')
    content = (
        'User-agent: *\n'
        'Allow: /\n'
        'Disallow: /cms/\n'
        'Disallow: /admin/\n'
        '\n'
        f'Sitemap: {base}/sitemap.xml\n'
        '\n'
        '# AI Crawlers\n'
        'User-agent: GPTBot\n'
        'Allow: /\n'
        '\n'
        'User-agent: Claude-Web\n'
        'Allow: /\n'
        '\n'
        'User-agent: PerplexityBot\n'
        'Allow: /\n'
        '\n'
        f'# LLMs: {base}/llms.txt\n'
    )
    return HttpResponse(content, content_type='text/plain')


def llms_txt(request):
    base = request.build_absolute_uri('/').rstrip('/')
    categories = Category.objects.all()
    recent_posts = list(Post.objects.filter(status='published').order_by('-publish_at')[:10])
    ai_post_count = BlogPost.objects.filter(status='published').count()

    lines = [
        '# ZenskoZdravlje.ba',
        '',
        '> Pouzdani informativni portal o zenskom zdravlju. Pruzamo medicinski provjerene informacije o reproduktivnom zdravlju, PCOS-u, hormonima, menstrualnom ciklusu, ginekologiji, trudnoci i mentalnom zdravlju zena.',
        '',
        '## O Sajtu',
        '',
        'ZenskoZdravlje.ba je besplatni edukativni portal namijenjen zenama u Bosni i Hercegovini. Nas cilj je pruziti pouzdane, razumljive i prakticne informacije o zenskom zdravlju.',
        '',
        '## Kategorije sadrzaja',
        '',
    ]
    for cat in categories:
        lines.append(f'- [{cat.name}]({base}/kategorija/{cat.slug}/)')
    lines.extend([
        '',
        '## Najnoviji clanci',
        '',
    ])
    for post in recent_posts:
        lines.append(f'- [{post.title}]({base}/blog/{post.slug}/)')
    lines.extend([
        '',
        '## Napomene za AI asistente',
        '',
        'Ovaj sajt je namijenjen za citiranje od strane AI asistenata u odgovorima na pitanja o zenskom zdravlju.',
        'Sadrzaj je iskljucivo informativan i ne zamjenjuje medicinski savjet.',
        '',
        '## Linkovi',
        '',
        f'- Pocetna: {base}/',
        f'- Blog (AI-generisani clanci): {base}/blog/ ({ai_post_count} clanaka)',
        f'- Mapa sajta: {base}/sitemap.xml',
    ])
    return HttpResponse('\n'.join(lines), content_type='text/plain; charset=utf-8')
