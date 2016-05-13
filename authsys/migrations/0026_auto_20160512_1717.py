# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0025_auto_20160510_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='a_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 12, 17, 17, 51, 74976), verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
    ]
