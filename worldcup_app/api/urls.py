from django.urls import path, include
from worldcup_app.api.views import MatchList

urlpatterns = [
    path('', MatchList.as_view(), name='matchlist'),
    ]