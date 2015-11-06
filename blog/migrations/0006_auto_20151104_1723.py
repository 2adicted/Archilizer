# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=b'ABC', unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=b'ABC', unique=True, max_length=40),
        ),
    ]
