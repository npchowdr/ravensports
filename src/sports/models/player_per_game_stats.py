from django.db import models

class PlayerPerGameStats(models.Model):
    Rank = models.IntegerField()
    Player = models.CharField(max_length=100)
    Position = models.CharField(max_length=10)
    Age = models.IntegerField()
    Team = models.CharField(max_length=5)
    GamesPlayed = models.IntegerField()
    GamesStarted = models.FloatField()
    MinutesPlayed = models.FloatField()
    FieldGoalsMade = models.FloatField()
    FieldGoalsAttempted = models.FloatField()
    FieldGoalPercentage = models.FloatField()
    ThreePointersMade = models.FloatField()
    ThreePointersAttempted = models.FloatField
    ThreePointPercentage = models.FloatField()
    TwoPointersMade = models.FloatField()
    TwoPointersAttempted = models.FloatField
    TwoPointPercentage = models.FloatField()
    EffectiveFieldGoalPercentage = models.FloatField()
    FreeThrowsMade = models.FloatField()
    FreeThrowsAttempted = models.FloatField
    FreeThrowPercentage = models.FloatField()
    OffensiveRebounds = models.FloatField()
    DefensiveRebounds = models.FloatField()
    TotalRebounds = models.FloatField()
    Assists = models.FloatField()
    Steals = models.FloatField()
    Blocks = models.FloatField()
    Turnovers = models.FloatField()
    PersonalFouls = models.FloatField()
    Points = models.FloatField()
    Year = models.IntegerField()

