# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userprofile_is_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_create',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_modify',
        ),
    ]
