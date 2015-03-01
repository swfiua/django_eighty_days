# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_eighty_days', '0005_auto_20150226_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammemberrequest',
            name='competitor',
        ),
        migrations.RemoveField(
            model_name='teammemberrequest',
            name='team',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='competitors',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_member_requests',
        ),
        migrations.DeleteModel(
            name='TeamMemberRequest',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_members',
        ),
        migrations.AddField(
            model_name='competitor',
            name='competition',
            field=models.ForeignKey(blank=True, related_name='competitors', to='django_eighty_days.Competition', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitor',
            name='team',
            field=models.ForeignKey(blank=True, related_name='team_members', to='django_eighty_days.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitor',
            name='team_member_request',
            field=models.ForeignKey(blank=True, related_name='team_member_requests', to='django_eighty_days.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='competition',
            field=models.ForeignKey(blank=True, related_name='teams', to='django_eighty_days.Competition', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(blank=True, related_name='workouts', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 3, 1)),
            preserve_default=True,
        ),
    ]
