# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_remove_trainingmodule_thumb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodule',
            name='name',
            field=models.CharField(default='management', max_length=30),
            preserve_default=False,
        ),
    ]
