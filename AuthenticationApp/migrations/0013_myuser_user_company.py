# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0012_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
