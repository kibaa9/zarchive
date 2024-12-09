from django.db import migrations


def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    content_type, _ = ContentType.objects.get_or_create(app_label='books', model='book')

    can_approve_books, _ = Permission.objects.get_or_create(
        codename='can_approve_books',
        name='Can approve books',
        content_type=content_type
    )

    admin_group, _ = Group.objects.get_or_create(name='Admin')
    staff_group, _ = Group.objects.get_or_create(name='Staff')

    admin_group.permissions.add(*Permission.objects.all())
    staff_group.permissions.add(can_approve_books)


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_approve_books', 'Can approve books')]},
        ),
        migrations.RunPython(create_groups_and_permissions),
    ]
