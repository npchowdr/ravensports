from django.db import models

class Standings(models.Model):
    teamId = models.IntegerField()
    win = models.IntegerField()
    loss = models.IntegerField()
    lastTenWin = models.IntegerField()
    lastTenLoss = models.IntegerField()
    streak = models.IntegerField()
    seasonYear = models.IntegerField()
    winPercentage = models.FloatField()
    homeWins = models.IntegerField()
    homeLoss = models.IntegerField()
    awayWins = models.IntegerField()
    awayLoss = models.IntegerField()
    winStreak = models.IntegerField()
