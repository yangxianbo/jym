# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0015_remove_upload_file_playtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_file',
            name='dotime',
        ),
        migrations.RemoveField(
            model_name='upload_file',
            name='filestate',
        ),
    ]
