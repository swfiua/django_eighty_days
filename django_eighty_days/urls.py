
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

    url(r'^activitys/$', api.ActivityList.as_view()),
    url(r'^activitys/(?P<pk>[0-9]+)/$', api.ActivityList.as_view(), name='activity-detail'),

    url(r'^competitions/$', api.CompetitionList.as_view()),
    url(r'^competitions/(?P<pk>[0-9]+)/$', api.CompetitionList.as_view(), name='competition-detail'),

    url(r'^competitors/$', api.CompetitorList.as_view()),
    url(r'^competitors/(?P<pk>[0-9]+)/$', api.CompetitorList.as_view(), name='competitor-detail'),

    url(r'^places/$', api.PlaceList.as_view()),
    url(r'^places/(?P<pk>[0-9]+)/$', api.PlaceList.as_view(), name='place-detail'),

    url(r'^routes/$', api.RouteList.as_view()),
    url(r'^routes/(?P<pk>[0-9]+)/$', api.RouteList.as_view(), name='route-detail'),

    url(r'^teams/$', api.TeamList.as_view()),
    url(r'^teams/(?P<pk>[0-9]+)/$', api.TeamList.as_view(), name='team-detail'),

    url(r'^teammembers/$', api.TeamMemberList.as_view()),
    url(r'^teammembers/(?P<pk>[0-9]+)/$', api.TeamMemberList.as_view(), name='teammember-detail'),

    url(r'^teammemberrequests/$', api.TeamMemberRequestList.as_view()),
    url(r'^teammemberrequests/(?P<pk>[0-9]+)/$', api.TeamMemberRequestList.as_view(), name='teammemberrequest-detail'),

    url(r'^workouts/$', api.WorkoutList.as_view()),
    url(r'^workouts/(?P<pk>[0-9]+)/$', api.WorkoutList.as_view(), name='workout-detail'),
]
#[[[end]]] (checksum: a173acc479c899ad2bc3ec5a849165b6)


urlpatterns = format_suffix_patterns(urlpatterns)
