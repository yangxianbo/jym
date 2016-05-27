# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0017_auto_20160524_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='playgroup',
            name='logourl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
