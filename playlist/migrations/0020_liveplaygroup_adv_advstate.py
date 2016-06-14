# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0019_auto_20160607_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveplaygroup_adv',
            name='advstate',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8\xe7\x8a\xb6\xe6\x80\x81'),
        ),
    ]
