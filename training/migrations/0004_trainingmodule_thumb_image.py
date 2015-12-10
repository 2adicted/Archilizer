# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20151116_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodule',
            name='thumb_image',
            field=models.ImageField(default='D:\test.jpg', upload_to=b'modules/'),
            preserve_default=False,
        ),
    ]
