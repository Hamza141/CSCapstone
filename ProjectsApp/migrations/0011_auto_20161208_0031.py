# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0010_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GroupsApp.Group'),
        ),
        migrations.AlterField(
            model_name='project',
            name='companies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company'),
        ),
    ]
