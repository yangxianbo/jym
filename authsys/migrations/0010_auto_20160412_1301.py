# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0009_auto_20160412_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorization',
            old_name='playlist',
            new_name='playid',
        ),
    ]
