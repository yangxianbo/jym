# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='dostate',
            field=models.IntegerField(verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='austate',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='autime',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x97\xb6\xe9\x95\xbf', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='dostate',
            field=models.IntegerField(null=True, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
    ]
