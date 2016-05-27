# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0012_remove_liveplaylist_playname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='liveplaylist',
        ),
    ]
