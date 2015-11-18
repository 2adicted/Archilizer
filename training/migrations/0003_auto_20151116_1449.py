# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20151109_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodule',
            name='image',
            field=models.ImageField(default='D:\x07rchilizer\\static_in_evn\\static_root\\img\\yemen.jpg', upload_to=b'modules/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainingmodule',
            name='level',
            field=models.CharField(max_length=30),
        ),
    ]
