from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('keyword', models.CharField(blank=True, max_length=255)),
                ('cluster', models.CharField(blank=True, db_index=True, max_length=120)),
                ('is_pillar', models.BooleanField(default=False)),
                ('pillar_slug', models.SlugField(blank=True, max_length=255)),
                ('intro', models.TextField(blank=True)),
                ('content_html', models.TextField(blank=True)),
                ('faq_json', models.JSONField(blank=True, null=True)),
                ('key_takeaways', models.JSONField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=255)),
                ('meta_description', models.CharField(blank=True, max_length=320)),
                ('internal_links', models.JSONField(blank=True, null=True)),
                ('quality_score', models.FloatField(default=0)),
                ('word_count', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], db_index=True, default='draft', max_length=20)),
                ('published_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AI Blog Post',
                'verbose_name_plural': 'AI Blog Posts',
                'ordering': ['-published_at', '-created_at'],
            },
        ),
    ]
