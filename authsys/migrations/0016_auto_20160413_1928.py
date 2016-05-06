# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0015_auto_20160413_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_file',
            old_name='filestate',
            new_name='status',
        ),
    ]
