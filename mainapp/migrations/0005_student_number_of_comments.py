# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20160703_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='number_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]