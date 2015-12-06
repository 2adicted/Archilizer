# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151106_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='D:\\konstrui-weblog.jpg', upload_to=b'blogposts/'),
            preserve_default=False,
        ),
    ]
