# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0002_appinfo_upstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinfo',
            name='ticker',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xaf', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='appdesc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='appfolder',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8c\x85\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='appid',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'APPID'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='appname',
            field=models.CharField(max_length=50, null=True, verbose_name=b'APP\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='appsize',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa4\xa7\xe5\xb0\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='downloadurl',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='upstate',
            field=models.CharField(default=1, max_length=50, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='uptime',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='version',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7', blank=True),
        ),
    ]
