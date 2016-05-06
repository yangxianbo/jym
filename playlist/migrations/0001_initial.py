# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='liveplaylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playaddress', models.CharField(max_length=255, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe5\x9c\xb0\xe5\x9d\x80')),
                ('classname', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('playname', models.CharField(max_length=255, null=True, verbose_name=b'\xe8\x8a\x82\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('playid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe8\x8a\x82\xe7\x9b\xaeID')),
            ],
        ),
        migrations.CreateModel(
            name='playgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=50, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('groupid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID')),
                ('groupdesc', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='upload_file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=255, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d')),
                ('filepath', models.CharField(max_length=255, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe8\xb7\xaf\xe5\xbe\x84')),
                ('playtype', models.CharField(max_length=20, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('filestate', models.CharField(default=1, max_length=20, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.AddField(
            model_name='liveplaylist',
            name='groupid',
            field=models.ForeignKey(related_name='live_list', to='playlist.playgroup'),
        ),
    ]
