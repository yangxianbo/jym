# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0009_playgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveplaylist',
            name='channelid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93ID', blank=True),
        ),
    ]
