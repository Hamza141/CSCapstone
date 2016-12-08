# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompaniesApp', '0002_auto_20161113_1721'),
        ('ProjectsApp', '0013_project_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='companyID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company'),
        ),
    ]