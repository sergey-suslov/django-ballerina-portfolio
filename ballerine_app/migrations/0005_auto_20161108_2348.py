# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballerine_app', '0004_gallery_minigallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minigallery',
            name='img',
        ),
        migrations.AddField(
            model_name='minigallery',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]