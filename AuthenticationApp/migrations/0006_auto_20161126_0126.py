# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0005_auto_20161126_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_engineer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
