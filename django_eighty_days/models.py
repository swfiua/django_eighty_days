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
    team_size = models.PositiveIntegerField()
    competitors = models.ManyToManyField('Competitor')
    teams = models.ManyToManyField('Team')

    def __str__(self):

        return self.name

class Competitor(models.Model):
    """ Competitor is a user competing in a competition """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=NAME_LENGTH)

    def __str__(self):

        return self.nickname


class Team(models.Model):
    """ A team entered in a competition """
    name = models.CharField(max_length=NAME_LENGTH)
    captain = models.ForeignKey(Competitor, related_name='captain')
    team_members = models.ManyToManyField('Competitor')
    team_member_requests = models.ManyToManyField('TeamMemberRequest', related_name='team_member_request')
    def __str__(self):

        return self.name


class TeamMemberRequest(models.Model):
    """ Handles requests to join a team """
    team = models.ForeignKey(Team)
    competitor = models.ForeignKey(Competitor)

    def __str__(self):

        return '/'.join(str(self.competitor), str(self.team))
    
    
    
# Places and routes -- should use GTFS
class Place(models.Model):
    pass
    
class Route(models.Model):
    pass

    
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


    def __str__(self):

        return '/'.join(str(self.activity), str(self.date))
