# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0010_auto_20160412_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorization',
            name='dotime',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
