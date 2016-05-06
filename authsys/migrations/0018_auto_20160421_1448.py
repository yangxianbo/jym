# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0017_auto_20160421_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine_info',
            name='groupid',
        ),
        migrations.AddField(
            model_name='machine_info',
            name='groupname',
            field=models.CharField(default=b'basegroup', unique=True, max_length=255, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d'),
        ),
    ]
