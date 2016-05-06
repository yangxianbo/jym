# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0012_auto_20160412_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_info',
            name='groupid',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\x88\x86\xe7\xbb\x84ID'),
        ),
        migrations.RemoveField(
            model_name='machine_info',
            name='groupid',
        ),
        migrations.AddField(
            model_name='machine_info',
            name='groupid',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\x88\x86\xe7\xbb\x84ID'),
        ),
    ]
