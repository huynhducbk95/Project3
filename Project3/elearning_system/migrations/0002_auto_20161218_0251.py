# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contribute_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='solve_number',
            field=models.IntegerField(default=0),
        ),
    ]