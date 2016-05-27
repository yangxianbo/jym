# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0016_auto_20160520_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveplaygroup',
            name='liverelate_id',
            field=models.TextField(default=b'', max_length=1000, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9a\x84\xe8\x8a\x82\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='liveplaylist',
            name='picurl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
