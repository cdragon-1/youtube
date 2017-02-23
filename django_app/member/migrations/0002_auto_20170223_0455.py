# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video', '__first__'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmarkvideo',
            old_name='myuser',
            new_name='user',
        ),
        migrations.AddField(
            model_name='bookmarkvideo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='bookmark_videos',
            field=models.ManyToManyField(blank=True, related_name='bookmark_user_set', through='member.BookmarkVideo', to='video.Video'),
        ),
    ]