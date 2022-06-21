from django.db import models

class Match(models.Model):
    match_group = models.CharField(("Group"), max_length=1)
    match_date = models.DateField(("Date"))
    match_time = models.TimeField(("Time"))
    home_team = models.CharField(("Home"), max_length=50)
    away_team = models.CharField(("Away"), max_length=50)
    home_goals = models.IntegerField(("Home Goals"))
    away_goals = models.IntegerField(("Away Goals"))
    
    def __str__(self):
        return (str(self.pk) + ' | ' + self.home_team + ' vs ' + self.away_team)

    class Meta:
        verbose_name_plural = "Matches"    