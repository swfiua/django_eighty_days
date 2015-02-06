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
        depth = 1

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition
        depth = 2

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitor
        depth = 1

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        depth = 1

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        depth = 1

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        depth = 1

class TeamMemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberRequest
        depth = 1

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workout
        depth = 1
#[[[end]]] (checksum: ae77f8b2859606bd94c4694d6641a9e4)
