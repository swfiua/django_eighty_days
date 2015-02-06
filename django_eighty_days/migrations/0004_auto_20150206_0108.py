# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0003_auto_20150204_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 2, 6)),
            preserve_default=True,
        ),
    ]
