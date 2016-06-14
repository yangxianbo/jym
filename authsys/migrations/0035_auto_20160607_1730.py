# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0034_pub_msg_timemsg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorization',
            name='playid',
        ),
        migrations.RemoveField(
            model_name='package_relateapp',
            name='playid',
        ),
        migrations.AddField(
            model_name='authorization',
            name='liveplayid',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9b\xb4\xe6\x92\xad\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='authorization',
            name='vodplayid',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x82\xb9\xe6\x92\xad\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='package_relateapp',
            name='liveplayid',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9b\xb4\xe6\x92\xad\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='package_relateapp',
            name='vodplayid',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x82\xb9\xe6\x92\xad\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
    ]
