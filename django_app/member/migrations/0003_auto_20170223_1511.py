# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        ('member', '0002_auto_20170223_0455'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmarkvideo',
            unique_together=set([('user', 'video')]),
        ),
    ]
