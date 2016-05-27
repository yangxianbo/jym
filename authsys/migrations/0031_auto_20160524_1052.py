# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0030_auto_20160523_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorization',
            name='blacklocation',
        ),
        migrations.RemoveField(
            model_name='machine_info',
            name='spare',
        ),
        migrations.AddField(
            model_name='authorization',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='machine_info',
            name='blacklocation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe9\x99\x90\xe5\x88\xb6', blank=True),
        ),
    ]
