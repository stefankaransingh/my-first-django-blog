# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-22 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(default=b'feature_images/None/no-img.jpg', upload_to=b'/feature_images'),
        ),
    ]
