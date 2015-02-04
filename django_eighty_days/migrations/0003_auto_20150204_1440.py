# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0002_auto_20150201_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='competitor',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='competition',
        ),
        migrations.AddField(
            model_name='competition',
            name='competitors',
            field=models.ManyToManyField(to='django_eighty_days.Competitor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(to='django_eighty_days.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='team_member_requests',
            field=models.ManyToManyField(to='django_eighty_days.TeamMemberRequest', related_name='team_member_request'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(to='django_eighty_days.Competitor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 2, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(to='django_eighty_days.Competitor', related_name='captain'),
            preserve_default=True,
        ),
    ]
