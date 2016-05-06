# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0021_auto_20160505_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
    ]
