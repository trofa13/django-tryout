# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20161110_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/treasure_images/placeholder.jpg', upload_to='treasure_images'),
        ),
    ]
