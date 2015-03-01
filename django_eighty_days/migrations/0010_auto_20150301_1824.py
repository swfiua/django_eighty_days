# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0009_remove_competitor_team_member_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member_requests',
        ),
        migrations.AddField(
            model_name='competitor',
            name='team_member_request',
            field=models.ForeignKey(blank=True, related_name='competitor', null=True, to='django_eighty_days.TeamMemberRequest'),
            preserve_default=True,
        ),
    ]
