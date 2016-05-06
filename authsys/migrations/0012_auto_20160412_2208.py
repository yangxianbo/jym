# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0011_authorization_dotime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorization',
            name='dostate',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='dotime',
            field=models.CharField(default=b'2016-04-01 00:00:00', max_length=255, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
