# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0024_auto_20160506_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_info',
            name='groupname',
        ),
        migrations.RemoveField(
            model_name='machine_info',
            name='groupname',
        ),
        migrations.AddField(
            model_name='machine_info',
            name='agency',
            field=models.CharField(default=b'baseagency', max_length=255, verbose_name=b'\xe4\xbb\xa3\xe7\x90\x86\xe5\x95\x86'),
        ),
        migrations.AlterField(
            model_name='group_info',
            name='agency',
            field=models.CharField(default=b'baseagency', unique=True, max_length=255, verbose_name=b'\xe4\xbb\xa3\xe7\x90\x86\xe5\x95\x86'),
        ),
    ]
