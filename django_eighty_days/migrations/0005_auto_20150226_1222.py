# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('django_eighty_days', '0004_auto_20150206_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='route',
            field=models.ForeignKey(related_name='competition', blank=True, to='django_eighty_days.Route', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default='nowhere', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='url',
            field=models.URLField(default='https://en.wikipedia.org/wiki/Around_the_World_in_Eighty_Days'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='description',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='places',
            field=models.ManyToManyField(related_name='route', to='django_eighty_days.Place'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='competitors',
            field=models.ManyToManyField(related_name='competition', to='django_eighty_days.Competitor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='start',
            field=models.DateField(default=datetime.date(2015, 2, 26)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(related_name='competition', to='django_eighty_days.Team', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competitor',
            name='user',
            field=models.ForeignKey(related_name='competitor', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member_requests',
            field=models.ManyToManyField(related_name='team_member_request', to='django_eighty_days.TeamMemberRequest', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(related_name='member', to='django_eighty_days.Competitor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teammemberrequest',
            name='team',
            field=models.ForeignKey(related_name='member_request', to='django_eighty_days.Team'),
            preserve_default=True,
        ),
    ]
