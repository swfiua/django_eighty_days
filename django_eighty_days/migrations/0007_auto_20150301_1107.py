# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0006_auto_20150301_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_members',
        ),
        migrations.RemoveField(
            model_name='teammemberrequest',
            name='competitor',
        ),
        migrations.AddField(
            model_name='competitor',
            name='team_member_request',
            field=models.ForeignKey(related_name='competitor', to='django_eighty_days.TeamMemberRequest', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competitor',
            name='team',
            field=models.ForeignKey(related_name='team_members', to='django_eighty_days.Team', blank=True, null=True),
            preserve_default=True,
        ),
    ]
