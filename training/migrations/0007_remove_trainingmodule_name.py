# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_trainingmodule_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingmodule',
            name='name',
        ),
    ]
