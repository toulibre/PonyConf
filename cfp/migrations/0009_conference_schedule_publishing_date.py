# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0008_auto_20170811_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='schedule_publishing_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Schedule publishing date'),
        ),
    ]
