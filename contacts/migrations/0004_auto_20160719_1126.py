# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20160718_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionstate',
            name='uuid',
            field=models.CharField(default=b'4da750a172154f1282bf3cd2083cd4bb', max_length=32, serialize=False, primary_key=True),
        ),
    ]
