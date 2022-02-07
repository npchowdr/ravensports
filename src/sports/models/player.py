from django.db import models

class Player(models.Model):
    playerId = models.IntegerField()
    fullName = models.CharField(max_length=50)
    TeamNickname = models.CharField(max_length=50)
