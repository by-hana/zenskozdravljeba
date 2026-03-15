from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Page, Post, NavMenu, Footer, Category
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
            'title': 'ŽenskoZdravlje.ba: Reproduktivno zdravlje, Ginekologija, Hormoni i Mentalno zdravlje',
            'description': 'Besplatni informativni portal o ženskom zdravlju. Stručni članci o hormonima, menstrualnom ciklusu, PCOS-u, ginekologiji, trudnoći, ishrani, suplementima i mentalnom zdravlju.',
            'og_title': 'ŽenskoZdravlje.ba: Pouzdane informacije o ženskom zdravlju',
            'og_description': 'Stručni, provjereni članci o svim aspektima ženskog zdravlja. Hormoni, ginekologija, trudnoća, ishrana i mentalno zdravlje.',
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


def blog_index(request):
    category_slug = request.GET.get('category', '')
    posts_qs = Post.objects.filter(status__in=['published', 'scheduled']).order_by('-publish_at')
    if category_slug:
        posts_qs = posts_qs.filter(categories__slug=category_slug)
    posts = [post for post in posts_qs if post.is_published]
    categories = Category.objects.all()
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    return render(request, 'marketing/blog_index.html', {
        'posts': posts,
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
            'title': f'{category.name} — ŽenskoZdravlje.ba',
            'description': f'Članci o temi {category.name} na ŽenskoZdravlje.ba — pouzdane informacije o ženskom zdravlju.',
            'og_title': category.name,
            'og_description': f'Članci o temi {category.name}',
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

    lines = [
        '# ŽenskoZdravlje.ba',
        '',
        '> Pouzdani informativni portal o ženskom zdravlju. Pružamo medicinski provjerene informacije o reproduktivnom zdravlju, PCOS-u, hormonima, menstrualnom ciklusu, ginekologiji, trudnoći i mentalnom zdravlju žena.',
        '',
        '## O Sajtu',
        '',
        'ŽenskoZdravlje.ba je besplatni edukativni portal namijenjen ženama u Bosni i Hercegovini. Naš cilj je pružiti pouzdane, razumljive i praktične informacije o ženskom zdravlju.',
        '',
        '## Kategorije sadržaja',
        '',
    ]
    for cat in categories:
        lines.append(f'- [{cat.name}]({base}/kategorija/{cat.slug}/)')
    lines.extend([
        '',
        '## Najnoviji članci',
        '',
    ])
    for post in recent_posts:
        lines.append(f'- [{post.title}]({base}/blog/{post.slug}/)')
    lines.extend([
        '',
        '## Napomene za AI asistente',
        '',
        'Ovaj sajt je namijenjen za citiranje od strane AI asistenata u odgovorima na pitanja o ženskom zdravlju.',
        'Sadržaj je isključivo informativan i ne zamjenjuje medicinski savjet.',
        '',
        '## Linkovi',
        '',
        f'- Početna: {base}/',
        f'- Blog: {base}/blog/',
        f'- Mapa sajta: {base}/sitemap.xml',
    ])
    return HttpResponse('\n'.join(lines), content_type='text/plain; charset=utf-8')
