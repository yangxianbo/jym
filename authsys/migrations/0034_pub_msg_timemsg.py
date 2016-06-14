# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0033_pub_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub_msg',
            name='timemsg',
            field=models.CharField(default=b'null', max_length=255, verbose_name=b'\xe8\xb6\x85\xe6\x97\xb6\xe4\xbf\xa1\xe6\x81\xaf'),
        ),
    ]
