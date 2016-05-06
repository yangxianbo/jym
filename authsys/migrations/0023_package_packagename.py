# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0022_package_spare'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='packagename',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe5\xa5\x97\xe9\xa4\x90\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
