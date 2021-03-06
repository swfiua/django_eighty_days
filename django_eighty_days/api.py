import datetime

import django_filters

from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django_eighty_days import models, serializers


"""[[[cog

from django_eighty_days import codegen

for name, clazz in codegen.get_models():

    cog.out(codegen.get_api_code(name))

]]]"""

class ActivityFilter(django_filters.FilterSet):
    """ Filtering Activity objects """
    class Meta:
        model = models.Activity
        fields = []

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
    filter_class = ActivityFilter

class CompetitionFilter(django_filters.FilterSet):
    """ Filtering Competition objects """
    class Meta:
        model = models.Competition
        fields = ['id', 'name']

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
    filter_class = CompetitionFilter

class CompetitorFilter(django_filters.FilterSet):
    """ Filtering Competitor objects """
    class Meta:
        model = models.Competitor
        fields = ['competition', 'user', 'team']

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
    filter_class = CompetitorFilter

class PlaceFilter(django_filters.FilterSet):
    """ Filtering Place objects """
    class Meta:
        model = models.Place
        fields = []

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
    filter_class = PlaceFilter

class RouteFilter(django_filters.FilterSet):
    """ Filtering Route objects """
    class Meta:
        model = models.Route
        fields = []

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
    filter_class = RouteFilter

class TeamFilter(django_filters.FilterSet):
    """ Filtering Team objects """
    class Meta:
        model = models.Team
        fields = ['competition']

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
    filter_class = TeamFilter

class TeamMemberRequestFilter(django_filters.FilterSet):
    """ Filtering TeamMemberRequest objects """
    class Meta:
        model = models.TeamMemberRequest
        fields = []

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
    filter_class = TeamMemberRequestFilter

class WorkoutFilter(django_filters.FilterSet):
    """ Filtering Workout objects """
    class Meta:
        model = models.Workout
        fields = []

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
    filter_class = WorkoutFilter
#[[[end]]] (checksum: f23efd424912cd40706e6bd01b0f2add)

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
def user_id(request):
    """ Return user object """

    user = request.user
    result = {}
    if not user.is_authenticated():
        result['id'] = 0
    else:
        result['id'] = user.id
    
    return Response(result)


@api_view(['GET'])
def get_everything_for_user(request, competition):
    """ Get all user data

    This is useful as we use the request to figure out the user and make sure
    they are logged on.
    """
    result = {}

    user = request.user

    print(competition)

    # don't return anything of not logged in
    if not user.is_authenticated():
        return Response({})

    # get competitors for this user
    competitor = models.Competitor.objects.filter(user=user, competition=competition)
    
    if competitor:
        result['competitor'] = serializers.CompetitorSerializer(competitor[0]).data
    else:
        result['competitor'] = {}
    
    return Response(result)


if __name__ == '__main__':
    # FIXME -- need to figureout how to test django apps

    import doctest

    doctest.testmod()
