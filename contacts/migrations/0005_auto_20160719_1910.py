# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20160719_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionstate',
            name='uuid',
            field=models.CharField(default=b'e2f47bcd14994b5084be5f463164cb71', max_length=32, serialize=False, primary_key=True),
        ),
    ]
