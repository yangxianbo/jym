# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0013_delete_liveplaylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='liveplaylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channelid', models.CharField(max_length=20, null=True, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93ID', blank=True)),
                ('playaddress', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('classname', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('playname', models.CharField(unique=True, max_length=255, verbose_name=b'\xe8\x8a\x82\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('mstatus', models.CharField(default=1, max_length=20, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe7\x8a\xb6\xe6\x80\x81')),
                ('picurl', models.CharField(max_length=255, null=True, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
            ],
        ),
    ]
