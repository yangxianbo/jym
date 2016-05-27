# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_auto_20160413_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveplaylist',
            name='mstatus',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AddField(
            model_name='liveplaylist',
            name='picurl',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
