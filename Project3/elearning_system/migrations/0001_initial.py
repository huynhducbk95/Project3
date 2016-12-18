# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseWebServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=30)),
                ('exercise_description', models.CharField(max_length=255)),
                ('view_number', models.IntegerField()),
                ('solve_number', models.IntegerField()),
                ('contributer_id', models.IntegerField()),
                ('approver_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('block_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.Role')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserSolveExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.ExerciseWebServer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.User')),
            ],
        ),
        migrations.AddField(
            model_name='exercisewebserver',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.Tag'),
        ),
        migrations.AddField(
            model_name='errormessage',
            name='reported_exercise_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.ExerciseWebServer'),
        ),
        migrations.AddField(
            model_name='errormessage',
            name='reporter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_system.User'),
        ),
    ]