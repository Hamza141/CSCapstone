# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0007_auto_20161126_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_university',
        ),
    ]