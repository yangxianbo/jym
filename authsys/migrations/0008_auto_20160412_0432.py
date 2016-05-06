# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0007_auto_20160412_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslog',
            name='appid',
            field=models.IntegerField(null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AddField(
            model_name='accesslog',
            name='cpuid',
            field=models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID'),
        ),
    ]
