# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0019_merge_20161208_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
