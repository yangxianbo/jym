# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0004_appinfo_logourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='downloadurl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='logourl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='ticker',
            field=models.TextField(default=b'', max_length=500, verbose_name=b'\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xaf'),
        ),
    ]
