from django.contrib import admin
from worldcup_app.models import *

class UserPredictionAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_edited',)

admin.site.register([Confederation, Tournament, Team, Match,])
admin.site.register(UserPrediction, UserPredictionAdmin)