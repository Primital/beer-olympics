from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    rules = models.TextField()


class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team_one = models.ForeignKey('players.Team', on_delete=models.CASCADE, related_name='match_team_one')
    team_two = models.ForeignKey('players.Team', on_delete=models.CASCADE, related_name='match_team_two')

