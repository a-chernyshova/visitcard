# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20170127_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
