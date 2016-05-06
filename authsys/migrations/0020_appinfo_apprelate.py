# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0019_auto_20160421_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='appinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(unique=True, max_length=50)),
                ('appname', models.CharField(max_length=255, null=True, blank=True)),
                ('appdesc', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='apprelate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(unique=True, max_length=255)),
                ('download_url', models.CharField(max_length=255, null=True, blank=True)),
                ('appid', models.ForeignKey(related_name='app_info', to='authsys.appinfo')),
            ],
        ),
    ]
