# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0016_auto_20160413_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_relateapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True)),
                ('playid', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x88\x97\xe8\xa1\xa8', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='authorization',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='group_info',
            name='groupid',
        ),
        migrations.AddField(
            model_name='group_info',
            name='agency',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbb\xa3\xe7\x90\x86\xe5\x95\x86', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='playid',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='group_relateapp',
            name='groupname',
            field=models.ForeignKey(related_name='group_relate_app', to='authsys.group_info'),
        ),
    ]
