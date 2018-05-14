from __future__ import unicode_literals

from django.db import migrations


GROUPS = [
    {
        "name": "ResourceInfoUser",
    },
    {
        "name": "ResourceInfoAdmin",
    },
]


def add_group_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = Group.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = Group.objects.get(
            name=group['name'],
        )
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('resourceinfo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_group_data,
            remove_group_data
        )
    ]
