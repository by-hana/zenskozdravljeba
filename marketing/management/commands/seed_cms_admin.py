from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create the CMS Admins group and an initial admin user'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='CMS Admins')
        if created:
            self.stdout.write('  Created "CMS Admins" group.')
        else:
            self.stdout.write('  "CMS Admins" group already exists.')

        # Create or get the admin user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@divineyoga.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write('  Created admin user (username: admin, password: admin123).')
        else:
            self.stdout.write('  Admin user already exists.')

        user.groups.add(group)
        self.stdout.write(self.style.SUCCESS('CMS admin setup complete.'))
