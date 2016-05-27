# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0011_auto_20160519_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveplaylist',
            name='playname',
        ),
    ]
