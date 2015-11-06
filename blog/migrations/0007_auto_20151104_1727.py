# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151104_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=40),
        ),
    ]
