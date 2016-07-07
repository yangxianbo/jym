# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0022_auto_20160706_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveplaygroup',
            name='livegroupid',
        ),
    ]
