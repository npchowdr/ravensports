from django.db import models

class Team(models.Model):
    teamId = models.IntegerField()
    city = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    shortName = models.CharField(max_length=50)
    allStar = models.BooleanField()
    nbaFranchise = models.BooleanField()
    league = models.CharField(max_length=50)
    confName = models.CharField(max_length=50)
    divName = models.CharField(max_length=50)