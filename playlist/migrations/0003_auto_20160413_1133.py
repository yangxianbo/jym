# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_auto_20160413_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_file',
            name='createtime',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='dotime',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\x84\xe7\x90\x86\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
