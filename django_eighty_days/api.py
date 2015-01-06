from django_eighty_days models, serializers

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CompetitionList(generics.ListCreateAPIView):
    """ Create or get Competition objects
    
    Without a pk, returns all Competition objects.

    With a pk, returns just that Competition
    """
    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer


class CompetitorList(generics.ListCreateAPIView):
    """ Create or get Competitor objects
    
    Without a pk, returns all Competitor objects.

    With a pk, returns just that Competitor
    """
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer


class TeamList(generics.ListCreateAPIView):
    """ Create or get Team objects
    
    Without a pk, returns all Team objects.

    With a pk, returns just that Team
    """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class TeamMemberList(generics.ListCreateAPIView):
    """ Create or get TeamMember objects
    
    Without a pk, returns all TeamMember objects.

    With a pk, returns just that TeamMember
    """
    queryset = models.TeamMember.objects.all()
    serializer_class = serializers.TeamMemberSerializer


class TeamMemberRequestList(generics.ListCreateAPIView):
    """ Create or get TeamMemberRequest objects
    
    Without a pk, returns all TeamMemberRequest objects.

    With a pk, returns just that TeamMemberRequest
    """
    queryset = models.TeamMemberRequest.objects.all()
    serializer_class = serializers.TeamMemberRequestSerializer

