from django_eighty_days models, serializers

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


"""[[[cog

from django_eighty_days import codegen

for name, clazz in codegen.get_models():

    cog.out(codegen.get_api_code(name))

]]]"""

class ActivityList(generics.ListCreateAPIView):
    """ Create or get Activity objects
    
    Without a pk, returns all Activity objects.

    With a pk, returns just that Activity
    """
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer

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

class PlaceList(generics.ListCreateAPIView):
    """ Create or get Place objects
    
    Without a pk, returns all Place objects.

    With a pk, returns just that Place
    """
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer

class RouteList(generics.ListCreateAPIView):
    """ Create or get Route objects
    
    Without a pk, returns all Route objects.

    With a pk, returns just that Route
    """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer

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

class WorkoutList(generics.ListCreateAPIView):
    """ Create or get Workout objects
    
    Without a pk, returns all Workout objects.

    With a pk, returns just that Workout
    """
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer
#[[[end]]] (checksum: 0bceace600ebefa13f4d33a43652ebd7)
