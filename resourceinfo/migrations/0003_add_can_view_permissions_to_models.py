# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resourceinfo', '0002_group_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['resource_id'], 'permissions': (('view_resource', 'Can view resource'),)},
        ),
    ]
