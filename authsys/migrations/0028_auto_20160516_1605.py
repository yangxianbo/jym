# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0027_auto_20160513_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apprelate',
            name='appid',
        ),
        migrations.DeleteModel(
            name='appinfo',
        ),
        migrations.DeleteModel(
            name='apprelate',
        ),
    ]
