# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0005_auto_20160518_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='liveplaygroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('livegroupname', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('livegroupid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID')),
                ('livegroupdesc', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('liverelate_id', models.TextField(max_length=500, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9a\x84\xe8\x8a\x82\xe7\x9b\xaeID', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='playgroup',
            name='groupdesc',
        ),
        migrations.RemoveField(
            model_name='playgroup',
            name='groupid',
        ),
        migrations.RemoveField(
            model_name='playgroup',
            name='groupname',
        ),
        migrations.RemoveField(
            model_name='playgroup',
            name='relate_id',
        ),
        migrations.AddField(
            model_name='playgroup',
            name='livegroupid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x9b\xb4\xe6\x92\xad\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID', blank=True),
        ),
        migrations.AddField(
            model_name='playgroup',
            name='vodgroupid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x82\xb9\xe6\x92\xad\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID', blank=True),
        ),
        migrations.AlterField(
            model_name='liveplaylist',
            name='playaddress',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='upload_file',
            name='filepath',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe8\xb7\xaf\xe5\xbe\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='upload_file',
            name='playtype',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
    ]
