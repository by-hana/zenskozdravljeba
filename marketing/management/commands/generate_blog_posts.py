"""
Django management command to generate 200 AI blog posts.

Usage:
  python manage.py generate_blog_posts                  # generate all 200
  python manage.py generate_blog_posts --count 10       # generate first 10
  python manage.py generate_blog_posts --cluster pcos   # one cluster only
  python manage.py generate_blog_posts --dry-run        # list keywords only
  python manage.py generate_blog_posts --pillars-only   # pillars first
"""

import random
import time
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from marketing.ai_generator import generate_outline, generate_article
from marketing.blog_keywords import ALL_POSTS, CLUSTERS, PILLAR_BY_CLUSTER
from marketing.models import BlogPost
from marketing.quality import score_article

RATE_LIMIT_SLEEP = 3    # seconds between API calls
BATCH_SIZE = 10         # posts per batch before a longer pause
BATCH_PAUSE = 30        # seconds between batches
PUBLISH_THRESHOLD = 85  # quality score to auto-publish


def random_published_at():
    """Random timestamp within the past 30 days."""
    days_ago = random.randint(0, 29)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)
    return timezone.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)


def get_related_posts(cluster: str, current_slug: str, limit: int = 3) -> list:
    """Return published BlogPost entries from same cluster for internal linking."""
    posts = BlogPost.objects.filter(
        cluster=cluster,
        status='published',
    ).exclude(slug=current_slug).values('slug', 'title')[:limit]
    return list(posts)


class Command(BaseCommand):
    help = 'Generate AI blog posts using Claude API'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=None,
                            help='Number of posts to generate (default: all)')
        parser.add_argument('--cluster', type=str, default=None,
                            help='Generate only posts from this cluster')
        parser.add_argument('--dry-run', action='store_true',
                            help='List keywords without generating')
        parser.add_argument('--pillars-only', action='store_true',
                            help='Generate only pillar articles')
        parser.add_argument('--skip-existing', action='store_true', default=True,
                            help='Skip posts that already exist in DB')
        parser.add_argument('--force', action='store_true',
                            help='Regenerate even if post already exists')

    def handle(self, *args, **options):
        posts_to_generate = list(ALL_POSTS)

        # Filter by cluster
        if options['cluster']:
            posts_to_generate = [p for p in posts_to_generate
                                  if p['cluster'] == options['cluster']]
            if not posts_to_generate:
                self.stderr.write(f"No posts found for cluster: {options['cluster']}")
                return

        # Filter pillars only
        if options['pillars_only']:
            posts_to_generate = [p for p in posts_to_generate if p['is_pillar']]

        # Limit count
        if options['count']:
            posts_to_generate = posts_to_generate[:options['count']]

        total = len(posts_to_generate)
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"ZenskoZdravlje.ba AI Blog Generator")
        self.stdout.write(f"Posts to generate: {total}")
        self.stdout.write(f"{'='*60}\n")

        if options['dry_run']:
            for i, post in enumerate(posts_to_generate, 1):
                pillar_mark = ' [PILLAR]' if post['is_pillar'] else ''
                self.stdout.write(f"{i:3}. [{post['cluster']}]{pillar_mark} {post['keyword']}")
            self.stdout.write(f"\nTotal: {total} posts")
            return

        # Sort: pillars first, then supporting (for internal link availability)
        posts_to_generate.sort(key=lambda p: (0 if p['is_pillar'] else 1))

        generated = 0
        skipped = 0
        failed = 0
        published = 0

        for i, post_data in enumerate(posts_to_generate, 1):
            slug = post_data['slug']
            keyword = post_data['keyword']
            cluster = post_data['cluster']
            is_pillar = post_data['is_pillar']

            # Skip existing (unless --force)
            if not options['force'] and BlogPost.objects.filter(slug=slug).exists():
                self.stdout.write(f"[{i}/{total}] SKIP (exists): {keyword}")
                skipped += 1
                continue

            self.stdout.write(f"\n[{i}/{total}] Generating: {keyword}")
            pillar_mark = ' (PILLAR)' if is_pillar else ''
            self.stdout.write(f"  Cluster: {cluster}{pillar_mark}")

            try:
                # Step 1: Generate outline
                self.stdout.write(f"  Step 1: Generating outline...")
                outline = generate_outline(keyword, cluster, is_pillar)
                time.sleep(RATE_LIMIT_SLEEP)

                # Get pillar info for internal links
                pillar_title = ''
                pillar_slug_val = ''
                if not is_pillar and cluster in PILLAR_BY_CLUSTER:
                    pillar_info = PILLAR_BY_CLUSTER[cluster]
                    pillar_slug_val = pillar_info['slug']
                    # Try to get title from DB
                    try:
                        pillar_obj = BlogPost.objects.get(slug=pillar_slug_val)
                        pillar_title = pillar_obj.title
                    except BlogPost.DoesNotExist:
                        pillar_title = pillar_info['keyword']

                related = get_related_posts(cluster, slug)

                # Step 2: Generate article
                self.stdout.write(f"  Step 2: Generating article...")
                article = generate_article(
                    outline=outline,
                    keyword=keyword,
                    is_pillar=is_pillar,
                    pillar_title=pillar_title,
                    pillar_slug=pillar_slug_val,
                    related_posts=related,
                )
                time.sleep(RATE_LIMIT_SLEEP)

                content_html = article.get('content_html', '')
                intro = article.get('intro', '')
                faq_json = article.get('faq_json', [])

                # Quality scoring
                quality, word_count = score_article(
                    content_html=content_html,
                    keyword=keyword,
                    faq_json=faq_json,
                    intro=intro,
                    is_pillar=is_pillar,
                )

                status = 'published' if quality >= PUBLISH_THRESHOLD else 'draft'
                pub_at = random_published_at() if status == 'published' else None

                # Build internal_links list
                internal_links = []
                if pillar_slug_val and pillar_title:
                    internal_links.append({'slug': pillar_slug_val, 'title': pillar_title, 'type': 'pillar'})
                for rp in related:
                    internal_links.append({'slug': rp['slug'], 'title': rp['title'], 'type': 'related'})

                # Save to DB
                obj, created = BlogPost.objects.update_or_create(
                    slug=slug,
                    defaults={
                        'title': outline.get('title', keyword),
                        'keyword': keyword,
                        'cluster': cluster,
                        'is_pillar': is_pillar,
                        'pillar_slug': pillar_slug_val,
                        'intro': intro,
                        'content_html': content_html,
                        'faq_json': faq_json,
                        'key_takeaways': outline.get('key_takeaways', []),
                        'meta_title': outline.get('meta_title', ''),
                        'meta_description': outline.get('meta_description', ''),
                        'internal_links': internal_links,
                        'quality_score': quality,
                        'word_count': word_count,
                        'status': status,
                        'published_at': pub_at,
                    },
                )

                action = 'Created' if created else 'Updated'
                status_icon = 'PUBLISHED' if status == 'published' else 'DRAFT'
                self.stdout.write(
                    f"  {action} | Score: {quality} | Words: {word_count} | {status_icon}"
                )
                generated += 1
                if status == 'published':
                    published += 1

                # Batch pause
                if generated % BATCH_SIZE == 0:
                    self.stdout.write(f"\n  Batch pause ({BATCH_PAUSE}s)...\n")
                    time.sleep(BATCH_PAUSE)

            except Exception as e:
                self.stderr.write(f"  FAILED: {e}")
                failed += 1
                time.sleep(5)

        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"DONE: Generated={generated} | Published={published} | "
                          f"Skipped={skipped} | Failed={failed}")
        self.stdout.write(f"{'='*60}\n")
