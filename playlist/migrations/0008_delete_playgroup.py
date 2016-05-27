# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0007_playgroup_groupid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='playgroup',
        ),
    ]
