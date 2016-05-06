# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accesslog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('aucode', models.CharField(max_length=255, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xa0\x81')),
                ('a_time', models.CharField(max_length=255, null=True, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('dostate', models.IntegerField(max_length=10, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.CreateModel(
            name='authorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(unique=True, max_length=25, verbose_name=b'MAC\xe7\xa0\x81')),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
                ('aucode', models.CharField(max_length=255, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xa0\x81')),
                ('s_time', models.CharField(default=b'2016-04-01 00:00:00', max_length=255, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('autime', models.IntegerField(max_length=255, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x97\xb6\xe9\x95\xbf', blank=True)),
                ('e_time', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('austate', models.IntegerField(default=1, max_length=10, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81')),
                ('playlist', models.CharField(default=1, max_length=50, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x88\x97\xe8\xa1\xa8')),
                ('agency', models.CharField(default=1, max_length=255, verbose_name=b'\xe4\xbb\xa3\xe7\x90\x86\xe5\x95\x86')),
                ('dostate', models.IntegerField(max_length=10, null=True, verbose_name=b'\xe9\x89\xb4\xe6\x9d\x83\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='perauthorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(unique=True, max_length=25, verbose_name=b'MAC\xe7\xa0\x81')),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
                ('register_time', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\xb7\xe6\xb1\x82\xe6\x97\xb6\xe9\x97\xb4')),
                ('perstate', models.IntegerField(default=1, max_length=10, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.AddField(
            model_name='accesslog',
            name='mac',
            field=models.ForeignKey(related_name='access_log', to='authsys.authorization'),
        ),
    ]
