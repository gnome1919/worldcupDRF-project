from rest_framework import serializers
from worldcup_app.models import Match


class MatchSerializer(serializers.ModelSerializer):
    # match_group = serializers.CharField(read_only=True)
    # match_date = serializers.CharField(read_only=True)
    # match_time = serializers.CharField(read_only=True)
    # home_team = serializers.CharField(read_only=True)
    # away_team = models.CharField(("Away"), max_length=50)
    # home_goals = models.IntegerField(("Home Goals"), max_length=2)
    # away_goals = models.IntegerField(("Away Goals"), max_length=2)

    class Meta:
        model = Match
        # exclude = ('watchlist',)
        fields = "__all__"