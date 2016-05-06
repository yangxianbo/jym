# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0008_auto_20160412_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_info',
            name='groupdesc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='appid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='dostate',
            field=models.CharField(max_length=20, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='appid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='austate',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='autime',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x97\xb6\xe9\x95\xbf', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='dostate',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='playlist',
            field=models.CharField(default=1, max_length=255, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x88\x97\xe8\xa1\xa8'),
        ),
        migrations.AlterField(
            model_name='perauthorization',
            name='appid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AlterField(
            model_name='perauthorization',
            name='perstate',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81'),
        ),
    ]
