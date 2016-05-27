# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0031_auto_20160524_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_info',
            name='blacklocation',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe9\x99\x90\xe5\x88\xb6'),
        ),
        migrations.AlterField(
            model_name='machine_info',
            name='blacklocation',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f\xe9\x99\x90\xe5\x88\xb6'),
        ),
    ]
