# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_trainingmodule_thumb_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingmodule',
            name='thumb_image',
        ),
    ]
