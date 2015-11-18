# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodule',
            name='attendants',
            field=models.DecimalField(default=1, max_digits=2, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='level',
            field=models.CharField(default='basic', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainingmodule',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]
