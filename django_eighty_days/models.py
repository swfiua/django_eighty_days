# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.conf import settings

# max length for names in models
NAME_LENGTH=200

# Teams and competitors
class Competition(models.Model):
    """ A competition

    Each competition consists of:

    Route
    Teams
    Activities
    Conditional activities: only allowed once you get to a place.
    """
    name  = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField()
    start = models.DateField(default=datetime.date.today())
    days = models.PositiveIntegerField(default=80)
    route = models.ForeignKey('Route', blank=True, null=True,
                              related_name='competition')
    
    team_size = models.PositiveIntegerField()

    serialize_depth = 2

    filter_fields = ['id', 'name']

    def __str__(self):

        return self.name

class Competitor(models.Model):
    """ Competitor is a user competing in a competition """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='competitor')
    nickname = models.CharField(max_length=NAME_LENGTH)

    competition = models.ForeignKey('Competition', related_name='competitors',
                                    blank=True, null=True)
    
    team = models.ForeignKey('Team', related_name='team_members',
                             blank=True, null=True)
    team_member_request = models.ForeignKey('Team', related_name='team_member_requests',
                                            blank=True, null=True)

    filter_fields = ['competition', 'user', 'team', 'team_member_request']

    def __str__(self):

        return self.nickname


class Team(models.Model):
    """ A team entered in a competition """
    name = models.CharField(max_length=NAME_LENGTH)
    captain = models.ForeignKey(Competitor, related_name='captain')
    competition = models.ForeignKey('Competition', related_name='teams',
                                    blank=True, null=True)
    
    filter_fields = ['competition']

    def __str__(self):

        return self.name

    
# Places and routes -- should use GTFS
class Place(models.Model):
    
    name = models.CharField(max_length=NAME_LENGTH, default="nowhere")
    latitude = models.FloatField(default=0.0)
    longitude =  models.FloatField(default=0.0)
    url = models.URLField(
        default="https://en.wikipedia.org/wiki/Around_the_World_in_Eighty_Days")
    
class Route(models.Model):

    name = models.CharField(max_length=NAME_LENGTH, default="")
    description = models.TextField(default="")

    places = models.ManyToManyField('Place', related_name='route')

    
# Activities
class Activity(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    units = models.CharField(max_length=NAME_LENGTH)
    miles_per_unit = models.FloatField()

    def __str__(self):

        return self.name
    
    
class Workout(models.Model):
    """ Each workout is an activity
    
    With a number of units and a date
    """
    activity = models.ForeignKey('Activity')
    units = models.FloatField()
    date = models.DateField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='workouts',
                             blank=True, null=True)

    def __str__(self):

        return '/'.join(str(self.activity), str(self.date))
