# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_hobbies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('specialization', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
    ]
