# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0006_auto_20160519_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='playgroup',
            name='groupid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID', blank=True),
        ),
    ]
