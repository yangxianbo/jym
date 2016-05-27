# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_auto_20160517_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveplaylist',
            name='groupid',
        ),
        migrations.RemoveField(
            model_name='liveplaylist',
            name='playid',
        ),
        migrations.AddField(
            model_name='playgroup',
            name='relate_id',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9a\x84\xe8\x8a\x82\xe7\x9b\xaeID', blank=True),
        ),
    ]
