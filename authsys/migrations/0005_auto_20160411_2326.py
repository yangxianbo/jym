# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0004_auto_20160411_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(unique=True, max_length=25, verbose_name=b'MAC\xe7\xa0\x81')),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
            ],
        ),
        migrations.CreateModel(
            name='premachine_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(unique=True, max_length=25, verbose_name=b'MAC\xe7\xa0\x81')),
                ('cpuid', models.CharField(default=b'ffffffff-d4bd-1afb-3ba9-893c0033c587', max_length=255, verbose_name=b'CPUID')),
            ],
        ),
        migrations.RemoveField(
            model_name='authorization',
            name='cpuid',
        ),
        migrations.AddField(
            model_name='authorization',
            name='appid',
            field=models.IntegerField(null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AddField(
            model_name='perauthorization',
            name='appid',
            field=models.IntegerField(null=True, verbose_name=b'APPID', blank=True),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='mac',
            field=models.ForeignKey(related_name='app_auth_info', to='authsys.machine_info'),
        ),
        migrations.AlterField(
            model_name='perauthorization',
            name='mac',
            field=models.ForeignKey(related_name='app_pre_info', to='authsys.premachine_info'),
        ),
    ]
