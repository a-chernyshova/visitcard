# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20170222_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='short_desc',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
