# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0022_auto_20161209_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='show',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='assigned_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='GroupsApp.Group'),
        ),
    ]