# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errormessage',
            old_name='reported_exercise_id',
            new_name='exercise_report',
        ),
        migrations.RenameField(
            model_name='errormessage',
            old_name='reporter_id',
            new_name='reporter',
        ),
        migrations.RenameField(
            model_name='exercisewebserver',
            old_name='approver_id',
            new_name='approver',
        ),
        migrations.RenameField(
            model_name='exercisewebserver',
            old_name='contributer_id',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='exercisewebserver',
            old_name='created_date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='exercisewebserver',
            old_name='tag_id',
            new_name='tag',
        ),
    ]
