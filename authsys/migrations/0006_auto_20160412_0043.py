# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0005_auto_20160411_2326'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='premachine_info',
            new_name='permachine_info',
        ),
    ]
