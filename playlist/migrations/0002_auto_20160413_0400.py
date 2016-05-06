# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveplaylist',
            name='groupid',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID'),
        ),
    ]
