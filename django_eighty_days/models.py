# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.apps import apps

# max length for names in models
NAME_LENGTH=200

# Get the user model
#UserModel = apps.get_model(settings.AUTH_USER_MODEL)

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
    team_size = models.PositiveIntegerField()

    def __str__(self):

        return self.name

    

class Competitor(models.Model):
    """ Competitor is a user competing in a competition """
    user = models.ForeignKey('users.User')
    nickname = models.CharField(max_length=NAME_LENGTH)
    competition = models.ForeignKey('Competition')

    def __str__(self):

        return self.nickname

class Team(models.Model):
    """ A team entered in a competition """
    name = models.CharField(max_length=NAME_LENGTH)
    captain = models.ForeignKey(Competitor)
    def __str__(self):

        return self.name

class TeamMember(models.Model):
    """ A team member is a competitor associcated with a team """
    competitor = models.ForeignKey(Competitor)
    team = models.ForeignKey(Team)

    def __str__(self):

        return '/'.join(str(self.competitor), str(self.team))


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
