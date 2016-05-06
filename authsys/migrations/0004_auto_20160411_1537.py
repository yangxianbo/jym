# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0003_auto_20160403_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='perauthorization',
            name='ipaddress',
            field=models.GenericIPAddressField(null=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe7\x9a\x84IP', blank=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='ipaddress',
            field=models.GenericIPAddressField(null=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe7\x9a\x84IP', blank=True),
        ),
    ]
