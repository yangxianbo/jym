# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0032_auto_20160524_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='pub_msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('successmsg', models.CharField(default=b'null', max_length=255, verbose_name=b'\xe6\x88\x90\xe5\x8a\x9f\xe4\xbf\xa1\xe6\x81\xaf')),
                ('errormsg', models.CharField(default=b'null', max_length=255, verbose_name=b'\xe5\xa4\xb1\xe8\xb4\xa5\xe4\xbf\xa1\xe6\x81\xaf')),
            ],
        ),
    ]
