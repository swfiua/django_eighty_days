from rest_framework import serializers
from django_eighty_days import models

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitor

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMember

class TeamMemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMemberRequest
