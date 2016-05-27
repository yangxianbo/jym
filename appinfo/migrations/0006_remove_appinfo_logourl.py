# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0005_auto_20160524_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinfo',
            name='logourl',
        ),
    ]
