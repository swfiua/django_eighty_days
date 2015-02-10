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

class ActivityCreate(generics.CreateAPIView):
    """ Create Activity object """
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Activity objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer

class ActivityList(generics.ListCreateAPIView):
    """ Create or get Activity objects
    
    returns all Activity objects.
    """
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer

class CompetitionCreate(generics.CreateAPIView):
    """ Create Competition object """
    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Competition objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer

class CompetitionList(generics.ListCreateAPIView):
    """ Create or get Competition objects
    
    returns all Competition objects.
    """
    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer

class CompetitorCreate(generics.CreateAPIView):
    """ Create Competitor object """
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer

class CompetitorDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Competitor objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer

class CompetitorList(generics.ListCreateAPIView):
    """ Create or get Competitor objects
    
    returns all Competitor objects.
    """
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer

class PlaceCreate(generics.CreateAPIView):
    """ Create Place object """
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Place objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer

class PlaceList(generics.ListCreateAPIView):
    """ Create or get Place objects
    
    returns all Place objects.
    """
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer

class RouteCreate(generics.CreateAPIView):
    """ Create Route object """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer

class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Route objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer

class RouteList(generics.ListCreateAPIView):
    """ Create or get Route objects
    
    returns all Route objects.
    """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer

class TeamCreate(generics.CreateAPIView):
    """ Create Team object """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Team objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamList(generics.ListCreateAPIView):
    """ Create or get Team objects
    
    returns all Team objects.
    """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamMemberRequestCreate(generics.CreateAPIView):
    """ Create TeamMemberRequest object """
    queryset = models.TeamMemberRequest.objects.all()
    serializer_class = serializers.TeamMemberRequestSerializer

class TeamMemberRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual TeamMemberRequest objects
    
    Supply pk of the object to work on.
    """
    queryset = models.TeamMemberRequest.objects.all()
    serializer_class = serializers.TeamMemberRequestSerializer

class TeamMemberRequestList(generics.ListCreateAPIView):
    """ Create or get TeamMemberRequest objects
    
    returns all TeamMemberRequest objects.
    """
    queryset = models.TeamMemberRequest.objects.all()
    serializer_class = serializers.TeamMemberRequestSerializer

class WorkoutCreate(generics.CreateAPIView):
    """ Create Workout object """
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete individual Workout objects
    
    Supply pk of the object to work on.
    """
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer

class WorkoutList(generics.ListCreateAPIView):
    """ Create or get Workout objects
    
    returns all Workout objects.
    """
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer
#[[[end]]] (checksum: 625c839d42525593b5350a1c48570092)

# Non cog-generated code below

# Monkey patch the Competitor create
def perform_competitor_create(self, serializer):
    serializer.save(user=self.request.user)

CompetitorCreate.perform_create=perform_competitor_create


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
    """ Get all user data

    FIXME -- probably don't need it now we have nested objects from rest-framework
    """
    result = {}

    user = request.user

    # don't return anything of not logged in
    if not user.is_authenticated():
        return Response({})

    # get competitors for this user
    competitors = models.Competitor.objects.filter(user=user)

    # Get competitions user is in
    competitions = []
    for competition in models.Competition.objects.all():
        for entered in competition.competitors.all():
            if entered in competitors:
                competitions.append(competition)

    # Get teams user is in and captain of
    captains = []
    teams = []
    for team in models.Team.objects.all():
        for competitor in competitors:
            if competitor in team.team_members.all():
                teams.append(team)
            if team.captain == competitor:
                captains.append(team)

    result['competitors'] = [serializers.CompetitorSerializer(x).data for x in competitors]
    result['competitions'] = [serializers.CompetitionSerializer(x).data for x in competitions]
    result['teams'] = [serializers.TeamSerializer(x).data for x in teams]
    result['captains'] = [serializers.TeamSerializer(x).data for x in captains]
    #result['user'] = user
    
    return Response(result)

@api_view(['POST'])
def add_competitor(request):
    """ Add a competitor to a competition """

    competitor_id =    int(request.data.get('competitor_id'))
    competition_id = int(request.data.get('competition_id'))

    competitor = models.Competitor.objects.get(pk=competitor_id)
    competition = models.Competition.objects.get(pk=competition_id)

    competition.competitors.add(competitor)
    competition.save()

    result = serializers.CompetitionSerializer(competition).data
    
    return Response(dict(competition=result))


if __name__ == '__main__':
    # FIXME -- need to figureout how to test django apps

    import doctest

    doctest.testmod()
