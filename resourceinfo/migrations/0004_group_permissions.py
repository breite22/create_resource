# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):

    Permission = apps.get_model('auth', 'Permission')
    resource_permissions = Permission.objects.filter(content_type__app_label='resourceinfo',
                                                       content_type__model='resource')

    perm_view_resource = Permission.objects.filter(content_type__app_label='resourceinfo',
                                                         content_type__model='resource',
                                                         codename='view_resource')

    resourceinfo_user_permissions = chain(perm_view_resource)

    admin_permissions = chain(resource_permissions)

    my_groups_initialization_list = [
        {
            "name": "ResourceInfoUser",
            "permissions_list": resourceinfo_user_permissions,
        },
        {
            "name": "ResourceInfoAdmin",
            "permissions_list": admin_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] != None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] != None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):

    dependencies = [
        ('resourceinfo', '0003_add_can_view_permissions_to_models'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
