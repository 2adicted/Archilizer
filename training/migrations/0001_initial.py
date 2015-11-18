# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=30)),
                ('short_description', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, max_length=40)),
                ('description', models.TextField()),
                ('objective', models.TextField()),
                ('structure', models.TextField()),
                ('duration', models.CharField(max_length=30, null=True, blank=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('location', models.CharField(max_length=30, blank=True)),
            ],
        ),
    ]
