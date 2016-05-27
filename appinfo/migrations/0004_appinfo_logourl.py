# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0003_auto_20160518_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinfo',
            name='logourl',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
