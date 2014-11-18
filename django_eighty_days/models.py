# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Competition(models.Model):
    name  = models.CharField(models.Model)
    description = models.TextField()

class Activity(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    miles_per_unit = models.FloatField()
    
class Workout(models.Model):
    activity = models.ForeignKey('Activity')
