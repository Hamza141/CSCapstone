# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0016_auto_20161208_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='createdBy',
        ),
    ]