# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='days',
            field=models.PositiveIntegerField(default=80),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 2, 1)),
            preserve_default=True,
        ),
    ]
