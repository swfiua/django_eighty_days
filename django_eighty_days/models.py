# -*- coding: utf-8 -*-

from django.db import models

class Place(models.Model):
    pass
    
class Route(models.Model):
    pass
    
class Competition(models.Model):
    name  = models.CharField(max_length=200)
    description = models.TextField()

class Activity(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    miles_per_unit = models.FloatField()
    
class Workout(models.Model):
    activity = models.ForeignKey('Activity')
