from worldcup_app.models import Match
from worldcup_app.api.serializers import MatchSerializer
from rest_framework import generics

class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    
    
