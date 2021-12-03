from django.db import models


class Team(models.Model):
      teamId = models.IntegerField()
      city = models.CharField(max_length=100)
      fullName = models.CharField(max_length=50)
      nickname = models.CharField(max_length=50)
      shortName = models.CharField(max_length=50)
      allStar = models.BooleanField()
      nbaFranchise = models.BooleanField()
      league = models.CharField(max_length=50)
      confName = models.CharField(max_length=50)
      divName = models.CharField(max_length=50)

      def __str__(self) -> str:
          return super().__str__()




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




      def __str__(self) -> str:
          return super().__str__()

