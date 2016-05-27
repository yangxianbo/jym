# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinfo',
            name='upstate',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
