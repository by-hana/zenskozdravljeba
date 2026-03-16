"""
Rescore all BlogPost entries using current quality.py logic,
and auto-publish those that meet the threshold.

Usage:
  python manage.py rescore_posts
  python manage.py rescore_posts --pillars-only
  python manage.py rescore_posts --dry-run
"""

from django.core.management.base import BaseCommand
from django.utils import timezone

from marketing.models import BlogPost
from marketing.quality import score_article

PUBLISH_THRESHOLD = 85


class Command(BaseCommand):
    help = 'Rescore BlogPost entries and auto-publish those meeting threshold'

    def add_arguments(self, parser):
        parser.add_argument('--pillars-only', action='store_true',
                            help='Only rescore pillar posts')
        parser.add_argument('--dry-run', action='store_true',
                            help='Show what would change without saving')

    def handle(self, *args, **options):
        qs = BlogPost.objects.all()
        if options['pillars_only']:
            qs = qs.filter(is_pillar=True)

        updated = 0
        published = 0

        for post in qs:
            old_score = post.quality_score
            old_status = post.status

            new_score, word_count = score_article(
                content_html=post.content_html or '',
                keyword=post.keyword or '',
                faq_json=post.faq_json,
                intro=post.intro or '',
                is_pillar=post.is_pillar,
            )

            new_status = 'published' if new_score >= PUBLISH_THRESHOLD else old_status

            if new_score != old_score or new_status != old_status:
                status_change = ''
                if new_status != old_status:
                    status_change = f' [{old_status.upper()} -> {new_status.upper()}]'
                self.stdout.write(
                    f"{'[DRY]' if options['dry_run'] else '[OK]'} "
                    f"{post.slug[:50]:<50} "
                    f"score: {old_score} -> {new_score} "
                    f"words: {word_count}{status_change}"
                )
                if not options['dry_run']:
                    post.quality_score = new_score
                    post.word_count = word_count
                    post.status = new_status
                    if new_status == 'published' and old_status != 'published':
                        post.published_at = post.published_at or timezone.now()
                        published += 1
                    post.save(update_fields=['quality_score', 'word_count', 'status', 'published_at'])
                updated += 1

        self.stdout.write(
            f"\nDone: {updated} posts rescored"
            + (f", {published} newly published" if published else "")
            + (" (dry run)" if options['dry_run'] else "")
        )
