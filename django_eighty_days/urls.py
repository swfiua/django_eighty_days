
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

    url(r'^activitys/$', api.ActivityList.as_view(), name='activity'),
    url(r'^activitys/(?P<pk>[0-9]+)/$', api.ActivityList.as_view(), name='activity-detail'),

    url(r'^competitions/$', api.CompetitionList.as_view(), name='competition'),
    url(r'^competitions/(?P<pk>[0-9]+)/$', api.CompetitionList.as_view(), name='competition-detail'),

    url(r'^competitors/$', api.CompetitorList.as_view(), name='competitor'),
    url(r'^competitors/(?P<pk>[0-9]+)/$', api.CompetitorList.as_view(), name='competitor-detail'),

    url(r'^places/$', api.PlaceList.as_view(), name='place'),
    url(r'^places/(?P<pk>[0-9]+)/$', api.PlaceList.as_view(), name='place-detail'),

    url(r'^routes/$', api.RouteList.as_view(), name='route'),
    url(r'^routes/(?P<pk>[0-9]+)/$', api.RouteList.as_view(), name='route-detail'),

    url(r'^teams/$', api.TeamList.as_view(), name='team'),
    url(r'^teams/(?P<pk>[0-9]+)/$', api.TeamList.as_view(), name='team-detail'),

    url(r'^teammemberrequests/$', api.TeamMemberRequestList.as_view(), name='teammemberrequest'),
    url(r'^teammemberrequests/(?P<pk>[0-9]+)/$', api.TeamMemberRequestList.as_view(), name='teammemberrequest-detail'),

    url(r'^workouts/$', api.WorkoutList.as_view(), name='workout'),
    url(r'^workouts/(?P<pk>[0-9]+)/$', api.WorkoutList.as_view(), name='workout-detail'),
]
#[[[end]]] (checksum: ad6a9305f322b9893939fa3931dbe49d)

urlpatterns += [
    url(r'^datetime_as_timestamp/$$', api.datetime_as_timestamp),
    url(r'^everything_for_user/$$', api.get_everything_for_user),
]

    
urlpatterns = format_suffix_patterns(urlpatterns)
