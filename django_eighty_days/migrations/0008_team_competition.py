# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0007_auto_20150301_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='competition',
            field=models.ForeignKey(null=True, related_name='teams', blank=True, to='django_eighty_days.Competition'),
            preserve_default=True,
        ),
    ]
