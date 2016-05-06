# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0023_package_packagename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_relateapp',
            old_name='groupname',
            new_name='packageid',
        ),
    ]
