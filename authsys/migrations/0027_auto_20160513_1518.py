# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0026_auto_20160512_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='preauthorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
                ('appid', models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True)),
                ('ipaddress', models.GenericIPAddressField(null=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe7\x9a\x84IP', blank=True)),
                ('register_time', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\xb7\xe6\xb1\x82\xe6\x97\xb6\xe9\x97\xb4')),
                ('prestate', models.CharField(default=1, max_length=20, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81')),
                ('spare', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='premachine_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(unique=True, max_length=25, verbose_name=b'MAC\xe7\xa0\x81')),
                ('macnum', models.CharField(max_length=25, null=True, verbose_name=b'\xe6\x95\xb0\xe5\xad\x97\xe7\xa0\x81', blank=True)),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
                ('spare', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perauthorization',
            name='mac',
        ),
        migrations.DeleteModel(
            name='perauthorization',
        ),
        migrations.DeleteModel(
            name='permachine_info',
        ),
        migrations.AddField(
            model_name='preauthorization',
            name='mac',
            field=models.ForeignKey(related_name='app_pre_info', to='authsys.premachine_info'),
        ),
    ]
