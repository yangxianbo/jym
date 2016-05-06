# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0013_auto_20160413_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=255, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d')),
                ('filepath', models.CharField(max_length=255, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe8\xb7\xaf\xe5\xbe\x84')),
                ('filestate', models.CharField(default=1, max_length=20, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\x84\xe7\x90\x86\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
    ]
