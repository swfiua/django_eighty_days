from django.contrib import admin
from django_eighty_days import models

admin.site.register(models.Competition)
admin.site.register(models.Competitor)
admin.site.register(models.Activity)
admin.site.register(models.Workout)
admin.site.register(models.Team)
admin.site.register(models.TeamMemberRequest)
