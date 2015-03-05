
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django_eighty_days import api

"""[[[cog

    from django_eighty_days import codegen

    cog.outl('urlpatterns = [')
    for name, clazz in codegen.get_models():

        cog.out(codegen.get_url_code(name))
    cog.outl(']')
    
]]]"""
urlpatterns = [

    url(r'^create_activity/$', api.ActivityCreate.as_view(), name='activity-create'),
    url(r'^detail_activitys/(?P<pk>[0-9]+)/$', api.ActivityDetail.as_view(), name='activity-detail'),
    url(r'^activitys/$', api.ActivityList.as_view(), name='activity-list'),

    url(r'^create_competition/$', api.CompetitionCreate.as_view(), name='competition-create'),
    url(r'^detail_competitions/(?P<pk>[0-9]+)/$', api.CompetitionDetail.as_view(), name='competition-detail'),
    url(r'^competitions/$', api.CompetitionList.as_view(), name='competition-list'),

    url(r'^create_competitor/$', api.CompetitorCreate.as_view(), name='competitor-create'),
    url(r'^detail_competitors/(?P<pk>[0-9]+)/$', api.CompetitorDetail.as_view(), name='competitor-detail'),
    url(r'^competitors/$', api.CompetitorList.as_view(), name='competitor-list'),

    url(r'^create_place/$', api.PlaceCreate.as_view(), name='place-create'),
    url(r'^detail_places/(?P<pk>[0-9]+)/$', api.PlaceDetail.as_view(), name='place-detail'),
    url(r'^places/$', api.PlaceList.as_view(), name='place-list'),

    url(r'^create_route/$', api.RouteCreate.as_view(), name='route-create'),
    url(r'^detail_routes/(?P<pk>[0-9]+)/$', api.RouteDetail.as_view(), name='route-detail'),
    url(r'^routes/$', api.RouteList.as_view(), name='route-list'),

    url(r'^create_team/$', api.TeamCreate.as_view(), name='team-create'),
    url(r'^detail_teams/(?P<pk>[0-9]+)/$', api.TeamDetail.as_view(), name='team-detail'),
    url(r'^teams/$', api.TeamList.as_view(), name='team-list'),

    url(r'^create_teammemberrequest/$', api.TeamMemberRequestCreate.as_view(), name='teammemberrequest-create'),
    url(r'^detail_teammemberrequests/(?P<pk>[0-9]+)/$', api.TeamMemberRequestDetail.as_view(), name='teammemberrequest-detail'),
    url(r'^teammemberrequests/$', api.TeamMemberRequestList.as_view(), name='teammemberrequest-list'),

    url(r'^create_workout/$', api.WorkoutCreate.as_view(), name='workout-create'),
    url(r'^detail_workouts/(?P<pk>[0-9]+)/$', api.WorkoutDetail.as_view(), name='workout-detail'),
    url(r'^workouts/$', api.WorkoutList.as_view(), name='workout-list'),
]
#[[[end]]] (checksum: 26dd5444f566c1bca6c8ba361ad3f3fe)

urlpatterns += [
    url(r'^datetime_as_timestamp/$$', api.datetime_as_timestamp),
    url(r'^everything_for_user/(?P<competition>[0-9]+)/$$', api.get_everything_for_user),
    url(r'^user_id/$$', api.user_id),
]

    
urlpatterns = format_suffix_patterns(urlpatterns)
