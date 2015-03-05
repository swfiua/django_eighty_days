# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0010_auto_20150301_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 3, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competitor',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='competitor'),
            preserve_default=True,
        ),
    ]
