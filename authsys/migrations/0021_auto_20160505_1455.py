# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0020_appinfo_apprelate'),
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('packageid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe5\xa5\x97\xe9\xa4\x90ID')),
                ('autime', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x97\xb6\xe9\x95\xbf', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='package_relateapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(max_length=20, null=True, verbose_name=b'APPID', blank=True)),
                ('playid', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x88\x97\xe8\xa1\xa8', blank=True)),
                ('groupname', models.ForeignKey(related_name='package_relate_app', to='authsys.package')),
            ],
        ),
        migrations.RemoveField(
            model_name='group_relateapp',
            name='groupname',
        ),
        migrations.AddField(
            model_name='accesslog',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='authorization',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='machine_info',
            name='macnum',
            field=models.CharField(max_length=25, null=True, verbose_name=b'\xe6\x95\xb0\xe5\xad\x97\xe7\xa0\x81', blank=True),
        ),
        migrations.AddField(
            model_name='machine_info',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='perauthorization',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='permachine_info',
            name='macnum',
            field=models.CharField(max_length=25, null=True, verbose_name=b'\xe6\x95\xb0\xe5\xad\x97\xe7\xa0\x81', blank=True),
        ),
        migrations.AddField(
            model_name='permachine_info',
            name='spare',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe7\x94\xa8\xe5\xad\x97\xe6\xae\xb5', blank=True),
        ),
        migrations.DeleteModel(
            name='group_relateapp',
        ),
    ]
