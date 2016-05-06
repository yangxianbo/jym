# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0002_auto_20160403_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perauthorization',
            name='perstate',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81'),
        ),
    ]
