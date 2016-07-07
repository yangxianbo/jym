# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0021_liveall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveplaylist',
            name='classname',
        ),
        migrations.AlterField(
            model_name='liveplaygroup',
            name='livegroupname',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
