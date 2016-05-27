# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0029_auto_20160517_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorization',
            name='spare',
        ),
        migrations.AddField(
            model_name='authorization',
            name='blacklocation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe9\x99\x90\xe5\x88\xb6', blank=True),
        ),
        migrations.AddField(
            model_name='group_info',
            name='blacklocation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe9\x99\x90\xe5\x88\xb6', blank=True),
        ),
    ]
