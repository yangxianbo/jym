# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0028_auto_20160516_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticker_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.TextField(max_length=500, null=True, verbose_name=b'\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xaf', blank=True)),
                ('tickerid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xafID')),
            ],
        ),
        migrations.AddField(
            model_name='group_info',
            name='tickerid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xafID', blank=True),
        ),
    ]
