from rest_framework import serializers
from django_eighty_days import models

"""[[[cog

from django_eighty_days import codegen

for name, clazz in codegen.get_models():

    cog.out(codegen.get_serializer_code(name))

]]]"""

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitor

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMember

class TeamMemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberRequest

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workout
#[[[end]]] (checksum: 8d776de98175cbe99f1106b0ae5af988)
