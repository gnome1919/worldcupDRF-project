from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Confederation(models.Model):
    name = models.CharField(max_length=8)
    
    def __str__(self):
        return (self.name)
    
    
class Tournament(models.Model):
    name = models.CharField('Name', max_length=200)
    confederation = models.ForeignKey(Confederation, on_delete=models.CASCADE)
    year = models.IntegerField('Year', validators=[MinValueValidator(2006),])
    
    def __str__(self):
        return (str(self.year) + ' | ' + self.name)
    

class Team(models.Model):
    name = models.CharField('Name', max_length=60)
    confederation = models.ForeignKey(Confederation, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.name)
    

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_matches')
    match_group = models.CharField('Group', max_length=1, blank=True)
    match_date = models.DateField('Date')
    match_time = models.TimeField('Time')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_teams_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_teams_matches')
    home_goals = models.IntegerField('Home Goals',validators=[MinValueValidator(0),MaxValueValidator(20)])
    away_goals = models.IntegerField('Away Goals',validators=[MinValueValidator(0),MaxValueValidator(20)])
    
    def __str__(self):
        return (str(self.tournament) + ' | ' + str(self.pk)  + ' | ' + str(self.home_team) + ' vs ' + str(self.away_team))

    class Meta:
        verbose_name_plural = 'Matches'
        
        
class UserPrediction(models.Model):
    user_prediction = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_predictions')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='user_predictions_matches')
    home_goals = models.IntegerField('Home Goals',validators=[MinValueValidator(0),MaxValueValidator(20)])
    away_goals = models.IntegerField('Away Goals',validators=[MinValueValidator(0),MaxValueValidator(20)])
    date_created = models.DateTimeField('Date Created',auto_now_add=True)
    date_edited = models.DateTimeField('Date Edited',auto_now=True)

    def __str__(self):
        return (str(self.user_prediction) + ' | ' + str(self.match.tournament) + ' | ' + str(self.match.pk)  +
                ' | ' + str(self.match.home_team) + ' vs ' + str(self.match.away_team))