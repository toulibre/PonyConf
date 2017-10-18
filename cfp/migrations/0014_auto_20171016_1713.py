# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-16 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0013_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='talk',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cfp.Tag'),
        ),
    ]