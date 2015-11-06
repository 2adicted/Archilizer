# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151103_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', null=True, through='blog.CategoryToPost', blank=True),
        ),
    ]
