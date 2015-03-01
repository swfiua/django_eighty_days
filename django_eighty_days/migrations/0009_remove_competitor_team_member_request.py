# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0008_team_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitor',
            name='team_member_request',
        ),
    ]
