from rest_framework import serializers
from django_eighty_days import models

"""[[[cog

from django_eighty_days import codegen

for name, clazz in codegen.get_models():
    cog.out(codegen.get_serializer_code(name, clazz))

]]]"""

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        depth = 0

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition
        depth = 0

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitor
        depth = 0

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        depth = 0

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        depth = 0

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        depth = 0

class TeamMemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberRequest
        depth = 0

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workout
        depth = 0
#[[[end]]] (checksum: 63eb3044c7da0c08f73703f9294deda2)
