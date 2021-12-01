from django.db import models
from django.db.models.fields import CharField
import requests


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
