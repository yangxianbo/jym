# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0018_auto_20160421_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine_info',
            name='groupname',
            field=models.CharField(default=b'basegroup', max_length=255, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d'),
        ),
    ]
