from django_eighty_days import models, serializers

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime

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

# Non cog-generated code below

@api_view(['GET'])    
def datetime_as_timestamp(request):
    """ Get date timestamps """

    result = {}
    result['now'] = unixtime(datetime.datetime.now()) * 1000

    return Response(result)

def unixtime(dt):
    """ Return the unixtime in seconds.

    Assumes dt is in UTC

    >>> unixtime(datetime.datetime(1970, 1, 1))
    0.0

    # Go forward a day = 24 * 3600 seconds
    >>> unixtime(datetime.datetime(1970, 1, 2))
    86400.0

    """
    return (dt - datetime.datetime(1970, 1, 1)).total_seconds()

@api_view(['GET'])
def get_everything_for_user(request):
    """ Get all user data """
    result = {}

    user = request.user

    # don't return anything of not logged in
    if not user.is_authenticated():
        return Response({})

    # Get competitions user is in
    competitions = user.competitor_set.all()

    # Get teams that user belongs to
    teams = models.TeamMember.objects.filter(competitor__in=competitions)

    # Get teams that user is captain of
    captains = models.Team.objects.filter(captain__in=competitions)
    
    result['competitions'] = [serializers.CompetitorSerializer(x).data for x in competitions]
    result['teams'] = [serializers.TeamMemberSerializer(x).data for x in teams]
    result['captains'] = [serializers.TeamSerializer(x).data for x in captains]

    return Response(result)

if __name__ == '__main__':
    # FIXME -- need to figureout how to test django apps

    import doctest

    doctest.testmod()
