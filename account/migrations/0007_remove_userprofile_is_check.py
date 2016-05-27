# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_check',
        ),
    ]
