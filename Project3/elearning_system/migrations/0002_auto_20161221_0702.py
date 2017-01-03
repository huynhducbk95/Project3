# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-21 06:12
from __future__ import unicode_literals

from django.db import migrations


def load_user_role(apps, schema_editor):
    Role = apps.get_model("elearning_system", "Role")
    User = apps.get_model("elearning_system", "User")

    admin_role = Role(role_name='admin')
    moderator_role = Role(role_name='moderator')
    user_role = Role(role_name='user')

    admin_role.save()
    moderator_role.save()
    user_role.save()

    admin_user = User(user_name='admin', password='admin', full_name='administrator',
                      email_address='amdin@elearning_system.com')
    admin_user.save()

    admin_user.role_set.add(admin_role, moderator_role, user_role)
    moderator_user = User(user_name='moderator', password='moderator', full_name='moderator',
                          email_address='moderator@elearning_system.com')
    moderator_user.save()
    moderator_user.role_set.add(moderator_role, user_role)


    moderator_user.save()

    admin_user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('elearning_system', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_user_role),
    ]