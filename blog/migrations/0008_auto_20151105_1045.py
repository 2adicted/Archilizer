# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151104_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(to='blog.Post', through='blog.CategoryToPost', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', through='blog.CategoryToPost', blank=True),
        ),
    ]
