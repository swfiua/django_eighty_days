# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0005_auto_20150226_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='competitors',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='teams',
        ),
        migrations.AddField(
            model_name='competitor',
            name='competition',
            field=models.ForeignKey(blank=True, null=True, related_name='competitors', to='django_eighty_days.Competition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitor',
            name='team',
            field=models.ForeignKey(blank=True, null=True, related_name='competitors', to='django_eighty_days.Team'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 3, 1)),
            preserve_default=True,
        ),
    ]
